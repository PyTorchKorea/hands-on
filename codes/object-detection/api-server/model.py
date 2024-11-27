# model.py

# Object Detection 모델들 중, Faster R-CNN 모델 불러오기
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_V2_Weights, fasterrcnn_resnet50_fpn_v2

# 앞에서 가져온 가중치를 제공하여 사전 학습된 모델 가져오기
def load_model_and_preprocess(device='cpu'):
  weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
  model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.5) # 기본값(0.5) 이상인 객체들을 탐지 후 필터링하여 반환
  model.to(device) # 지정된 장치로 모델 이동
  model.eval()     # (학습이 아닌) 추론 모드로 설정

  return model, weights.transforms(), weights.meta


if __name__ == '__main__':
  model, preprocess, meta = load_model_and_preprocess()
  print(model)
  print(preprocess)
  print(meta)
