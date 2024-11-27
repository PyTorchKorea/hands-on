# ⌨️ REST API 구현하기

## REST API 개요

앞에서 사용해본 Faster R-CNN 사전학습 모델을 가지고 REST API를 만들어보겠습니다. 클라이언트는 HTTP 요청을 통해 이미지를 서버로 전송하고, 서버는 Faster R-CNN 모델을 사용하여 객체 탐지 결과를 반환하려고 합니다.

기본적인 REST API 개발 경험이 있다고 가정하고, HTTP나 RESTful 등에 대해서는 따로 설명을 하지 않겠습니다. 이러한 개념들이 익숙치 않으시다면 도서나 웹 페이지, 유튜브 등을 통해 별도로 학습해주세요.

```{note}
REST API는 Google Colab 같은 Notebook 환경이 아닌, 로컬 환경에서 진행해야 합니다.
```

프레임워크로는 FastAPI를 사용하겠습니다. Flask를 사용한 예제는 아래 **"Flask로 배포하기(Deploying with Flask)"** 튜토리얼을 참고해주세요:

- 원본 튜토리얼(영문): https://pytorch.org/tutorials/recipes/deployment_with_flask.html
- 번역 튜토리얼(국문): https://tutorials.pytorch.kr/recipes/deployment_with_flask.html

```{warning}
이 랩의 모든 코드는 학습을 목적으로 작성하였습니다. 서비스를 고려하지 않았으니 학습용으로만 사용해주세요.
```
