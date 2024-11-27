(object-detection:intro-object-detection)=
# 📚 객체 탐지 소개

## 객체 탐지와 컴퓨터 비전

객체 탐지(Object Detection)는 이미지나 동영상에서 특정 객체(들)을 식별하고, 식별한 객체가 위치한 영역을 표시하는 컴퓨터 비전(Computer Vision) 작업 중 하나입니다. 이는 인공지능 모델이 카메라를 들고 화면에 보이는 물체들을 찾아서 표시하고, 각 물체들에 이름표를 붙이는 작업을 하는 것으로 비유할 수 있습니다.

이러한 객체 탐지 기술은 X-Ray나 MRI, CT 영상 등으로부터 병변을 탐지하는 의료 영상 분석 또는 도로 위의 차량이나 보행자, 신호 등을 탐지하는 자율주행 시스템 등에 활용됩니다.

\
객체 탐지는 컴퓨터 비전의 여러 응용 분야 중 하나로, 이미지 분류(Classification)와 이미지 세분화(Segmentation)와 밀접한 연관이 있습니다. 예를 들어, 객체 탐지는 이미지 분류를 넘어 여러 객체를 탐지하고 각 객체의 위치를 제공하며, 이미지 세분화는 탐지된 객체의 경계까지 정확히 정의합니다. 입력/출력 데이터의 형태를 바탕으로 간단히 각 작업을 비교하면 다음과 같습니다:

|작업|정의|입력 데이터|출력 데이터|주요 활용 사례|
|---|---|---|---|---|
|이미지 분류 (Classification)|이미지에서 하나의 객체 카테고리를 예측|단일 이미지|단일 라벨|이미지 검색, 동물 종류 분류|
|객체 탐지 (Object Detection)|여러 객체의 존재 여부와 위치를 바운딩 박스로 예측|단일 이미지|여러 라벨과 바운딩 박스|자율주행 차량, 감시 시스템|
|이미지 세분화 (Segmentation)|이미지의 모든 픽셀을 객체 영역으로 할당|단일 이미지|픽셀 단위 마스크|의료 영상 분석, 자율주행 정밀 지도 생성|

\
각 작업(Task)을 한 문장으로 정리하면 다음과 같습니다.
- 이미지 분류는 단순히 "이 이미지는 무엇인가?"라는 질문에 답합니다.
- 객체 탐지는 "무엇이 어디에 있는가?"라는 질문을 해결합니다.
- 이미지 세분화는 "무엇이 어디에 있는가?"라는 질문에 픽셀 수준의 정밀한 결과를 제공합니다.

\
컴퓨터 비전(Computer Vision)과 관련한 더 다양한 작업들은 [PapersWithCode 사이트](https://paperswithcode.com/)를 참고해주세요:

```{figure} images/paperswithcode-sota.png
---
alt: PapersWithCode 사이트의 Browse State-of-the-Art 메뉴
name: PapersWithCode 사이트
width: 640px
align: center
---
바로가기: [https://paperswithcode.com/area/computer-vision](https://paperswithcode.com/area/computer-vision)
```

```{note}
새로운 분야의 연구나 기술을 탐색할 때, PapersWithCode 사이트는 매우 유용한 정보를 제공합니다.
주요 분야들에 대한 최신 연구 논문과 코드, 그리고 성능 평가 지표 등을 한눈에 확인할 수 있습니다.
```


## 객체 탐지 랩 소개

이번 객체 탐지 랩에서는 PyTorch의 영상처리 특화 라이브러리(Domain API)인 torchvision을 활용합니다. torchvision을 사용하여 이미지를 불러오고, 변환하기 위한 방법들을 코드를 통해 배워봅니다. 이후, 사전 학습된 모델을 사용하고 개선하는 방법을 익혀보겠습니다.
