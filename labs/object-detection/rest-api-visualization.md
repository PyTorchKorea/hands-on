# ⌨️ API 호출 결과 시각화

## 시각화를 위한 client 구성

검출한 객체를 시각화하여 확인해보겠습니다. 다음과 같이 별도의 공간에 `client.py` 파일을 생성하고, 객체 탐지 요청 및 결과 시각화를 위한 코드를 작성합니다.
다음과 같이 구성하였습니다:
```text
object-detection-client       # 객체 탐지 결과 시각화를 위한 클라이언트
├── client.py                 # 객체 탐지 요청 및 결과 시각화 코드
└── data                      # 객체 탐지의 입력 및 결과 이미지 저장 공간
    └── sample.jpg            # 객체 탐지를 수행할 예제 이미지
```

API 호출을 위해 `requests` 라이브러리를 사용하므로, 설치가 되어 있지 않다면 다음과 같이 설치합니다:
```bash
pip install requests
```

## `client.py` 작성

이제 검출된 객체를 시각화하여 저장하도록 `client.py`를 다음과 같이 작성합니다:
```python
import random
import collections

import requests
import json
import torch
import torchvision

from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.v2 import functional as F

import matplotlib.pyplot as plt

# 이미지 파일 경로 지정
fn_img_input = 'data/sample.jpg'
fn_img_output = 'data/sample_output.jpg'

# REST API 호출
url = 'http://localhost:8000/image:detect'
payload = {'threshold': 0.8}
files = [
    ('image', ('sample.jpg', open(fn_img_input, 'rb'), 'image/jpeg'))
]
response = requests.post(url, data=payload, files=files)
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    print(response.text)

# 탐지 결과
results = json.loads(response.text)

# 결과 변환
objects_types = [result['label'] for result in results['objects']]
objects_counter = collections.Counter(objects_types)
color_type = {result['class']:("#%06x" % random.randint(0, 0xFFFFFF)) for result in results['objects']}
box_coords = torch.stack([torch.tensor(result['bbox']) for result in results['objects']])
box_labels = [f"{result['label']}({result['score']:.2f})" for result in results['objects']]
box_colors = [color_type[result['class']] for result in results['objects']]

# 주요 결과 출력
print(f'검출된 객체 수: {len(results["objects"])}')
print(f'검출된 객체 종류: {objects_counter}')

# 이미지에 검출 결과 그리기
tensor_with_boxes = draw_bounding_boxes(torchvision.io.read_image(fn_img_input),
                                        boxes=box_coords,
                                        labels=box_labels,
                                        colors=box_colors,
                                        font='Verdana',
                                        font_size=20,
                                        width=2,)

# 검출 결과가 그려진 Tensor를 PIL.Image로 변환하여 저장
F.to_pil_image(tensor_with_boxes).save(fn_img_output)
```

실행 결과는 `fn_img_output`에 지정한 경로(`data/sample_output.jpg`)에 저장됩니다. 저장된 이미지를 확인하여 객체 탐지 결과를 시각화할 수 있습니다.

## 객체 탐재 결과 시각화

이제 `client.py`를 실행하여 객체 탐지 결과를 확인해보겠습니다. [첫번째 예시 이미지](https://unsplash.com/photos/people-walking-at-walkway-Q6-jv031muY)의 객체 탐지 결과 시각화 결과입니다:

```{figure} images/restapi-sample-input1.jpg
---
alt: 객체 탐지에 사용한 첫번째 예시 이미지
name: 객체 탐지에 사용한 첫번째 예시 이미지
width: 640px
align: center
---
[Matt Quinn이 Unsplash 공개한 이미지](https://unsplash.com/photos/people-walking-at-walkway-Q6-jv031muY)를 첫번째 예시 이미지로 사용합니다.
```

```bash
$ python client.py
검출된 객체 수: 23
검출된 객체 종류: Counter({'person': 14, 'handbag': 6, 'backpack': 2, 'cell phone': 1})
```

```{figure} images/restapi-sample-output1.jpg
---
alt: 첫번째 예시 이미지의 객체 탐지 결과 시각화 결과
name: 첫번째 예시 이미지의 객체 탐지 결과 시각화 결과
width: 800px
align: center
---
[첫번째 예시 이미지](https://unsplash.com/photos/people-walking-at-walkway-Q6-jv031muY)의 객체 탐지 결과 시각화 결과입니다.
```

[다른 예시 이미지](https://unsplash.com/photos/a-group-of-people-walking-down-a-flight-of-stairs-jEEP-bzH3jI)의 결과도 한 번 확인해보겠습니다:
```{figure} images/restapi-sample-input2.jpg
---
alt: 객체 탐지에 사용한 두번째 예시 이미지
name: 객체 탐지에 사용한 두번째 예시 이미지
width: 640px
align: center
---
[wu yi가 Unsplash 공개한 이미지](https://unsplash.com/photos/a-group-of-people-walking-down-a-flight-of-stairs-jEEP-bzH3jI)를 두번째 예시 이미지로 사용합니다.
```

```bash
$ python client.py
검출된 객체 수: 45
검출된 객체 종류: Counter({'person': 32, 'handbag': 10, 'backpack': 3})
```

```{figure} images/restapi-sample-output2.jpg
---
alt: 두번째 예시 이미지의 객체 탐지 결과 시각화 결과
name: 두번째 예시 이미지의 객체 탐지 결과 시각화 결과
width: 800px
align: center
---
[두번째 예시 이미지](https://unsplash.com/photos/a-group-of-people-walking-down-a-flight-of-stairs-jEEP-bzH3jI)의 객체 탐지 결과 시각화 결과입니다.
```
