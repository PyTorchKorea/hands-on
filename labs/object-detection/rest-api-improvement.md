# ⌨️ API 모델 개선하기

## 특정 객체만 탐지하도록 변경하기

현재 객체 탐지 API는 이미지에 있는 모든 객체를 탐지합니다. 하지만 사용자가 특정 객체만 탐지하도록 요청할 수 있도록 API를 개선해보겠습니다.
요청 매개변수에 `klass` 매개변수를 추가하여 탐지된 객체 중에서 특정 클래스 이름을 가진 객체만 반환하도록 합니다. (`class`는 파이썬 예약어이므로 `klass`를 매개변수 이름으로 사용합니다.)

즉, 아래와 같이 요청 매개변수를 변경합니다:

**요청 매개변수**

| 매개변수 | 형태 | 필수 여부 | 설명 |    |
| ------ | --- | ------ | --- | -- |
| *threshold*  | `float` |     | *최소 신뢰 점수(0.5 ~ 1.0, 기본값: 0.5)<br />주어진 수치보다 크거나 같은 신뢰 점수(Confidence Score)를 갖는 객체들만 반환* | |
| **klass**  | `int` |     | 탐지할 객체의 Class ID | **추가** |

기본적인 동작은 `threshold`와 비슷합니다. 객체 탐지 결과의 `score` 값이 `threshold`보다 크거나 같은 객체들만 반환하는 것처럼, `class` 매개변수를 추가하여 탐지된 객체 중에서 특정 클래스 이름을 가진 객체만 반환하도록 합니다.

```{note}
`class` 매개변수는 탐지된 객체의 클래스 ID를 의미합니다. 클래스 ID는 객체 탐지 모델이 학습된 클래스의 순서대로 0부터 시작하는 정수입니다.
실제로는 2개 이상의 `class` 매개변수를 지정할 수 있도록 확장해보세요.
```

## `util.py`에 함수 추가하기

`util.py`에 결과 필터링 함수 `filter_results()`를 개선하여 객체 탐지 결과 중에서 특정 클래스 ID를 가진 객체만 반환하도록 합니다. `klass` 매개변수를 추가하고, `klass` 값이 주어진 경우, `klass`와 일치하지 않는 결과는 무시합니다:

```python
# 결과 필터링 함수
def filter_results(outputs, categories, threshold=0.5, klass=None):
  filtered_results = []

  for label, score, box in zip(outputs['labels'], outputs['scores'], outputs['boxes']):
    # threshold 값보다 작은 score를 갖는 탐지 결과는 무시
    if score < threshold:
      continue

    # klass 값이 주어진 경우, klass와 일치하지 않는 결과는 무시
    if klass is not None and int(label) != klass:
      continue

    filtered_results.append({
      "class": int(label),
      "label": categories[int(label)],
      "score": float(score),
      "bbox": [float(coord) for coord in box]
    })

  return filtered_results
```

## `app.py` 엔드포인트 변경하기

`/image:detect` 엔드포인트의 요청 본문을 처리하는 `predict()` 함수를 개선하여 `klass` 매개변수를 추가하고, `util.py`의 `filter_results()` 함수를 사용하여 결과를 필터링합니다:

```python
# 객체 탐지 엔드포인트
@app.post("/image:detect")
def detect_objects(image: UploadFile, threshold: float = 0.5, klass: int = None):
  try:
    # 이미지 파일이 아닌 경우 예외 발생
    if not image.headers['content-type'].startswith('image/'):
      raise ValueError("Uploaded file is not an image")

    # 클래스 ID가 주어진 경우, 유효한 클래스 ID인지 확인
    if klass is not None and klass < 0:
      raise ValueError("Invalid class ID")

    # 업로드된 이미지 파일 열기 (PIL.Image 객체로 변환)
    img_obj = Image.open(BytesIO(image.file.read()))

    # 전처리
    img_input = preprocess(img_obj).to(device)
    img_input = img_input.unsqueeze(0) # 단일 이미지이므로 배치(batch) 차원 추가

    # 추론 수행
    outputs = model(img_input)[0] # 단일 이미지이므로 첫번째 결과만 사용

    # 결과 필터링
    results = filter_results(outputs, meta['categories'], threshold=threshold, klass=klass)

    return JSONResponse(content={"objects": results})
  except ValueError as e:
    return JSONResponse(content={"error": str(e)}, status_code=415)
  except Exception as e:
    return JSONResponse(content={"error": str(e)}, status_code=500)
```

## 동작 확인하기

변경된 API를 테스트해보겠습니다. Swagger UI에서 `klass` 매개변수를 사용하여 특정 클래스 ID를 가진 객체만 탐지하도록 요청합니다:
```{figure} images/restapi-swagger-improved.png
---
alt: klass 매개변수를 추가한 FastAPI의 Swagger UI 화면
name: FastAPI의 Swagger UI - klass 매개변수 추가
width: 640px
align: center
---
FastAPI의 Swagger UI에서 klass 매개변수를 추가 설정하여 객체 탐지 결과를 필터링할 수 있습니다.
```

또는, 아래와 같이 `client.py`를 아래와 같이 변경하여 사용하는 것도 가능합니다:
```python
# REST API 호출
url = 'http://localhost:8000/image:detect?threshold=0.8&klass=1'
files = [
    ('image', ('sample.jpg', open(fn_img_input, 'rb'), 'image/jpeg'))
]
```

`klass`가 `1(person)`인 객체를 탐지하도록 요청한 결과는 다음과 같습니다:


```{figure} images/restapi-improved-sample-output1.jpg
---
alt: 첫번째 예시 이미지의 사람 객체 탐지 결과 시각화 결과
name: 첫번째 예시 이미지의 사람 객체 탐지 결과 시각화 결과
width: 800px
align: center
---
[첫번째 예시 이미지](https://unsplash.com/photos/people-walking-at-walkway-Q6-jv031muY)에서 사람 객체만 탐지하도록 한 결과 시각화 결과입니다.
```



```{figure} images/restapi-improved-sample-output2.jpg
---
alt: 두번째 예시 이미지의 사람 객체 탐지 결과 시각화 결과
name: 두번째 예시 이미지의 사람 객체 탐지 결과 시각화 결과
width: 800px
align: center
---
[두번째 예시 이미지](https://unsplash.com/photos/a-group-of-people-walking-down-a-flight-of-stairs-jEEP-bzH3jI)에서 사람 객체만 탐지하도록 한 결과 시각화 결과입니다.
```

## 다른 개선 방향

실제 서비스에 활용하기 위해서는 아직 더 개선할 부분이 많습니다. 몇 가지 개선 방향을 제시하겠습니다:

- `klass` 매개변수를 확장하여 2개 이상의 클래스 ID를 지정할 수 있도록 확장합니다.
- 하나 이상의 객체 탐지 모델을 사용할 수 있도록 확장합니다.
- 객체 탐지 결과를 시각화하여 반환하는 기능을 추가합니다.
- 객체 탐지 결과를 데이터베이스에 저장하고, 이력을 관리할 수 있는 기능을 추가합니다.
- 길거리의 이동 인구를 탐지하는 등, 웹캠 또는 영상을 입력으로 받아 객체 탐자 결과를 수행합니다.


이 외에도 다양한 개선 방향이 있습니다. 여러분의 서비스에 맞게 API를 개선해보세요.

## 코드 및 질문/답변

이 랩의 최종 코드는 [여기](https://github.com/PyTorchKorea/hands-on/blob/master/codes/object-detection/)에서 확인하실 수 있습니다.