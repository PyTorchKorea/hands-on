# 📚 PyTorch와 torchvision

## PyTorch 소개

PyTorch는 Python에 익숙한 분들이 쉽게 사용하실 수 있는 인공지능 프레임워크로, 직관적이고 유연하게 동작하도록 설계된 것이 특징입니다. 다른 딥러닝 프레임워크로는 Tensorflow나 Jax, MXNet 등이 있지만, PyTorch를 익혀야 하는 가장 큰 이유는 "PyTorch가 많이 사용되기 때문"입니다.

PapersWithCode 통계에 따르면, 최근 몇 년간의 연구 논문과 오픈소스 저장소에서 사용된 딥러닝 프레임워크의 50% 이상이 PyTorch를 기반으로 합니다. 즉, PyTorch로 모델을 직접 만들고 학습하지 않더라도, 다양한 사전 학습 모델들을 활용하기 위해서는 PyTorch를 익히는 것이 필요합니다.

PyTorch에 대한 더 자세한 소개는 PyTorch 공식 사이트와 파이토치 한국 사용자 모임 등을 확인해주세요:
- PyTorch 공식 사이트: https://pytorch.org
- PyTorch 공식 튜토리얼: https://pytorch.org/tutorials
- 파이토치 한국 사용자 모임: https://pytorch.kr
- 파이토치 한국어 튜토리얼: https://tutorials.pytorch.kr

\
PyTorch는 다양한 분야(Domain)에서 활용할 수 있는 특화 라이브러리들도 제공합니다. 이 라이브러리들은 특정 데이터 유형이나 문제 도메인에 초점을 맞추고 있으며, 주요 라이브러리는 다음과 같습니다:

- torchvision: 이미지 처리와 컴퓨터 비전
- torchtext: 텍스트 데이터와 자연어 처리(NLP)
- torchaudio: 오디오 데이터와 신호 처리

이 중 이미지 처리와 컴퓨터 비전 모델을 쉽게 활용할 수 있도록 도와주는 torchvision에 대해서 더 알아보겠습니다.

## torchvision 소개

torchvision은 PyTorch의 도메인 라이브러리 중 하나로, 이미지 처리 및 컴퓨터 비전 작업을 쉽게 수행할 수 있도록 지원합니다. 이 라이브러리는 다음과 같은 주요 기능을 제공합니다:

- 데이터셋 관리: 유명한 공개 데이터셋의 다운로드 및 로드
- 사전 학습된 모델: 컴퓨터 비전에서 자주 사용되는 딥러닝 모델 제공
- 데이터 전처리 및 변환: 이미지 증강과 전처리 파이프라인 구축
- 컴퓨터 비전 연산: NMS, RoI Align 등 컴퓨터 비전 특화 연산 지원

이러한 기능을 제공하기 위해 torchvision는 다양한 모듈들로 구성되어 있습니다. 주요 모듈 및 역할은 다음과 같습니다:

| 모듈 | 역할 |
| :--- | :--- |
| `torchvision.datasets` | 다양한 이미지 및 비디오 데이터셋을 제공하는 모듈로, 간편하게 데이터셋을 로드하고 사용할 수 있습니다. 유명한 데이터셋인 CIFAR, MNIST, ImageNet 등이 포함됩니다. |
| `torchvision.io` | 이미지와 비디오 데이터를 읽고 쓰는 입출력 기능을 제공하는 모듈입니다. 데이터를 텐서로 변환하여 모델 학습에 사용하기 쉽게 해줍니다. |
| `torchvision.models` | 미리 학습된 다양한 딥러닝 모델 아키텍처를 제공하는 모듈입니다. ResNet, AlexNet, VGG, EfficientNet 등 여러 CNN 모델을 쉽게 불러와 사용할 수 있습니다. |
| `torchvision.ops` | 컴퓨터 비전 작업에 유용한 다양한 연산을 제공하는 모듈입니다. RoI Align, NMS (Non-Maximum Suppression) 등 특정 작업에 최적화된 연산 함수를 포함하고 있습니다. |
| `torchvision.transforms` | 이미지 데이터에 대한 전처리와 변환 기능을 제공하는 모듈입니다. 데이터 증강 (augmentation) 및 정규화 등 다양한 변환을 손쉽게 적용할 수 있습니다. |
| `torchvision.utils` | 이미지 데이터를 시각화하거나 텐서 데이터를 다루기 위한 다양한 유틸리티 함수를 제공하는 모듈입니다. 예를 들어, `make_grid` 함수는 여러 이미지를 격자 형태로 묶어 보여줄 수 있습니다. |
