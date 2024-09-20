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

#### CG값 추출

#### FFT 적용 및 관심 주파수 설정

#### 관심 주파수 영역 iFFT 적용

#### 맥박 RR 간격 검출 후 맥박 계산

### 눈 감은 시간 측정 구현

#### 눈 사이의 간격 측정

#### 눈 감은 시간 측정




## 주요 기능

### [Create]

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%82%AD%EC%A0%9C%20%EA%B2%B0%EA%B3%BC.jpg" width="700" height="200"/>

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%20%EB%93%B1%EB%A1%9D2.jpg" width="400" height="400"/>

+ 질문 등록 버튼을 눌러 새로운 질문을 등록할 수 있습니다.


### [Read]

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%EB%AA%A9%EB%A1%9D.jpg" width="700" height="200"/>

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%EC%83%81%EC%84%B8.jpg" width="700" height="200"/>  

+ 등록된 질문을 선택하여 상세 정보를 볼 수 있습니다.

### [Update]

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%EC%88%98%EC%A0%95.jpg" width="400" height="400"/>

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%EC%88%98%EC%A0%95%EC%83%81%EC%84%B8.jpg" width="700" height="200"/>  

+ 수정 버튼을 눌러 질문의 정보를 변경할 수 있습니다.

### [Delete]

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%A7%88%EB%AC%B8%EC%82%AD%EC%A0%9C.jpg" width="700" height="200"/>

<img src="https://github.com/wqp99w/read-me_image/blob/main/webserver/%EC%82%AD%EC%A0%9C%20%EA%B2%B0%EA%B3%BC.jpg" width="700" height="200"/>  

+ 삭제 버튼을 눌러 질문을 삭제할 수 있습니다.

