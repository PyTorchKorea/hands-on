# API 구현: `app.py`

마지막으로 API를 구현하는 `app.py`를 작성합니다. 이 파일은 FastAPI를 사용하여 API를 구현합니다.

```python
# app.py
from io import BytesIO

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import torch
import torchvision

from model import load_model_and_preprocess
from utils import filter_results

# FastAPI 앱 생성
app = FastAPI()

# 모델 불러오기
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, preprocess, meta = load_model_and_preprocess(device)

# 모델 정보 관리
models = [
  {
    "id": model.__class__.__module__,
    "name": type(model).__name__
  }
]

# 모델 정보 엔드포인트
@app.get("/models")
def get_models():
  return JSONResponse(content={"models": models})

# 객체 탐지 엔드포인트
@app.post("/image:detect")
def detect_objects(image: UploadFile, threshold: float = 0.5):
  try:
    # 이미지 파일이 아닌 경우 예외 발생
    if not image.headers['content-type'].startswith('image/'):
      raise ValueError("Uploaded file is not an image")

    # 업로드된 이미지 파일 열기 (PIL.Image 객체로 변환)
    img_obj = Image.open(BytesIO(image.file.read()))

    # 전처리
    img_input = preprocess(img_obj).to(device)
    img_input = img_input.unsqueeze(0) # 단일 이미지이므로 배치(batch) 차원 추가

    # 추론 수행
    outputs = model(img_input)[0] # 단일 이미지이므로 첫번째 결과만 사용

    # 결과 필터링
    results = filter_results(outputs, meta['categories'], threshold=threshold)

    return JSONResponse(content={"objects": results})
  except ValueError as e:
    return JSONResponse(content={"error": str(e)}, status_code=415)
  except Exception as e:
    return JSONResponse(content={"error": str(e)}, status_code=500)
```