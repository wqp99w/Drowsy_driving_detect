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

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### CG값 추출

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### FFT 적용 및 관심 주파수 설정

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### 관심 주파수 영역 iFFT 적용

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### 맥박 RR 간격 검출 후 맥박 계산

### 눈 감은 시간 측정 구현

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### 눈 사이의 간격 측정

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)

#### 눈 감은 시간 측정

![기능분석도](https://github.com/wqp99w/read-me_image/blob/main/cpastone/%EA%B8%B0%EB%8A%A5%EB%B6%84%EC%84%9D%EB%8F%84.jpg)


