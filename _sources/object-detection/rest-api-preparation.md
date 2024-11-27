# 객체 탐지 API 구성

REST API를 설계할 때는 API가 어떤 기능을 제공하고, 이를 어떻게 클라이언트가 요청 및 응답 형식으로 사용할 수 있는지 정의하는 것이 중요합니다. 다음과 같이 2개의 엔드포인트(endpoint)를 갖는 객체 탐지 REST API를 만들어보겠습니다:

| URI | Method | 개요 |
| --- | ------ | --- |
| /models | GET | 모델 정보 |
| /image:detect | POST | 객체 탐지 |

## 모델 정보

**Endpoint**

- `GET /models`

**설명**

- 사용 가능한 모델 정보를 요청합니다.

**요청 헤더**

| Key | Value |
| --- | ----- |
| Content-Type | multipart/form-data |

**요청 매개변수**

- 없음

```{note}
작업의 종류나 모델 이름 등으로 검색할 수 있도록 매개변수를 추가해보세요!
```

**응답 코드**

| Code | Status | 설명 |
| ---- | ------ | --- |
| 200  | OK     | 성공 |
| 500  | Internal Error | 실패(서버 문제) |

**응답 본문**

| 매개변수 | 형태 | 설명 |
| ---- | ------ | --- |
| models | array | 사용 가능한 모델(`model` 객체) 목록 |


`model` 객체는 다음과 같이 구성됩니다:

| 매개변수 | 형태 | 설명 |
| ------ | --- | ----|
| id    | string | 식별 가능한 모델의 고유한 ID |
| name  | string | (사람을 위한) 모델의 이름 |


**예시**

- 요청 예시 \
   `GET /models`

- 응답 예시 (200 OK)
   ```json
   {
    "models": [
      {
        "id": "fasterrcnn",
        "name": "Faster R-CNN"
      },
      {
        "id": "anothermodelid",
        "name" "Another Model Name"
      }
    ]
   }
   ```


## 객체 탐지

**Endpoint**

- `POST /image:detect`

**설명**

객체 탐지를 수행합니다.

**요청 매개변수**

| 매개변수 | 형태 | 필수 여부 | 설명 |
| ------ | --- | ------ | --- |
| threshold  | `float` |     | 최소 신뢰 점수(0.5 ~ 1.0, 기본값: 0.5)<br />주어진 수치보다 크거나 같은 신뢰 점수(Confidence Score)를 갖는 객체들만 반환 |

**요청 본문**

| 매개변수 | 형태 | 필수 여부 | 설명 |
| ------ | --- | ------ | --- |
| image  | `file` | 필수 | 이미지 파일 |

```{note}
특정 객체만 탐지하도록 하거나, 탐지된 객체의 수를 제한하는 등의 매개변수를 추가해보세요!
```

**응답 코드**

| Code | Status | 설명 |
| ---- | ------ | --- |
| 200  | OK     | 성공 |
| 400  | Bad Request | 잘못된 요청 |
| 415  | Unsupported Media Type | 잘못된 요청 |

**응답 본문**

| 매개변수 | 형태 | 설명 |
| ---- | ------ | --- |
| objects | array | 탐지한 객체(`object` 객체) 목록 |

`object` 객체는 다음과 같이 구성됩니다:

| 매개변수 | 형태 | 설명 |
| ------ | --- | ----|
| class  | integer | 탐지한 객체 종류(ID) |
| label  | string | (사람을 위한) 탐지한 객체 종류(이름) |
| score  | float | 신뢰도 점수 |
| bbox   | array | 객체 위치를 표시하는 좌표 [x1, y1, x2, y2]<br />좌측 상단(x1, y1), 우측 하단(x2, y2)의 x, y 좌표 |

**예시**

- 요청 예시 \
   `POST /image:detect`
   ```
    {
      "image": @이미지파일,
      "threshold": 0.6
    }
   ```

- 응답 예시 (200 OK)
   ```json
   {
    "objects": [
      {
        "class": 1,
        "label": "person",
        "score": 0.85,
        "bbox": [50, 100, 200, 250]
      },
      {
        "class": 1,
        "label": "person",
        "score": 0.65,
        "bbox": [150, 200, 400, 450]
      }
    ]
   }
   ```

- 응답 예시 (400 Bad Request, 415 Unsupported Media Type)
  ```json
  {
    "code": 415,
    "error": "File format not supported"
  }
  ```

