# 사용자의 피부 영상을 통한 졸음운전방지 시스템

2024.06

## 프로젝트 개요

졸음 운전 사고가 날이 갈 수록 증가하는 추세이기 때문에 이를 방지하기 위해 대형화물차량이나 졸음운전방지 기능이 없는 중저가형 차량들을 위한 졸음운전 사고방지 시스템을 설게하였습니다.
사용자의 피부 영상을 통해 맥박수를 측정하고, 이를 통해 졸음 운전을 감지합니다. 또한 추가적으로 눈을 일정시간 동안 감고 있으면 이를 통해서도 졸음 운전을 감지하도록 설계하였습니다.

## 개발 환경

+ Python, OpenCV, dlib
+ IDE : VS Code

## 기능 분석도

### 간략화된 기능 분석도

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

### 구체화된 기능 분석도 1

![기능분석도1](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%841.jpg)

### 구체화된 기능 분석도 2

![기능분석도2](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%842.jpg)



## 구현 과정

### 피부 영상을 통한 맥박 측정 구현

#### 랜드마크 검출 및 관심 영역 설정

![얼굴관심영역설](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EC%96%BC%EA%B5%B4%EA%B4%80%EC%8B%AC%EC%98%81%EC%97%AD%EC%84%A4%EC%A0%95.jpg)

#### CG값 추출

![CG값 추출](https://github.com/wqp99w/read-me_image/blob/main/cpastone/CG%EA%B0%92%EC%B6%94%EC%B6%9C.jpg)

#### FFT 적용 및 관심 주파수 설정

![FFT 적용](https://github.com/wqp99w/read-me_image/blob/main/cpastone/FFT.jpg)

#### 관심 주파수 영역 iFFT 적용

![iFFT](https://github.com/wqp99w/read-me_image/blob/main/cpastone/iFFT.jpg)

#### 맥박 RR 간격 검출 후 맥박 계산

![맥박공식](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EB%A7%A5%EB%B0%95%EC%88%98%EA%B3%B5%EC%8B%9D.jpg)

![맥박결과](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EB%A7%A5%EB%B0%95%EA%B2%B0%EA%B3%BC.jpg)


### 눈 감은 시간 측정 구현

![눈사이간격](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EB%88%88%EC%82%AC%EC%9D%B4%EA%B0%84%EA%B2%A9.jpg)

#### 눈 사이의 간격/시 측정

![눈 간격 결과](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EB%88%88%EA%B0%84%EA%B2%A9%EA%B2%B0%EA%B3%BC.jpg)



