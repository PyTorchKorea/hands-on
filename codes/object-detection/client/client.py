import io
import random
import collections

import requests
import json
import torch
import torchvision

from PIL import Image

# 시각화 등을 위해 필요한 라이브러리 불러오기
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.v2 import functional as F

import matplotlib.pyplot as plt

# 이미지 파일
fn_img_input = 'data/sample.jpg'
fn_img_output = 'data/sample_output.jpg'

# REST API 호출
url = 'http://localhost:8000/image:detect?threshold=0.8&klass=1'
files = [
    ('image', ('sample.jpg', open(fn_img_input, 'rb'), 'image/jpeg'))
]
response = requests.post(url, files=files)
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    print(response.text)

# 결과 확인
results = json.loads(response.text)
objects_types = [result['label'] for result in results['objects']]
objects_counter = collections.Counter(objects_types)
color_type = {result['class']:("#%06x" % random.randint(0, 0xFFFFFF)) for result in results['objects']}
box_coords = torch.stack([torch.tensor(result['bbox']) for result in results['objects']])
box_labels = [f"{result['label']}({result['score']:.2f})" for result in results['objects']]
box_colors = [color_type[result['class']] for result in results['objects']]

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
F.to_pil_image(tensor_with_boxes).save(fn_img_output)
print(f'검출 결과 이미지 저장: {fn_img_output}')