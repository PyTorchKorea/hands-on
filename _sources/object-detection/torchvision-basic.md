# ⌨️ torchvision 기초

torchvision을 사용하여 이미지를 불러오고, 변환(전처리)하는 기본 작업들을 다룹니다. 데이터셋을 불러오고 데이터 증강(augmentation)과 같은 작업은 컴퓨터 비전 모델 학습의 필수적인 단계입니다.

## PyTorch 및 torchvision 설치

```{note}
Google Colab을 사용 중이라면 별도의 설치 과정이 필요 없습니다.
```

먼저, torchvision이 설치되어 있는지 확인하고, 설치되지 않았다면 아래 명령어로 설치합니다.

```bash
pip install torch torchvision
```
