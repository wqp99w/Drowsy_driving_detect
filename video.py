import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pygame
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
MOUTH = list(range(48, 68))
NOSE = list(range(27, 36))
EYEBROWS = list(range(17, 27))
JAWLINE = list(range(1, 17))
ALL = list(range(0, 68))
EYES = list(range(36, 48))


def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

#면적 찍을 때 점 간격들
dx=[-3,0,3,-3,3,-3,0,3]
dy=[-3,-3,-3,0,0,3,3,3]

fixed_size = (500, 500)  # 얼굴 고정할 크기

#-- 데이터 파일과 이미지 파일 경로
predictor_file = './working/shape_predictor_68_face_landmarks.dat' 
image_file = './image/sleep.jpg' 
audio_file='./audio/siren.mp3'

detector = dlib.get_frontal_face_detector() #얼굴 감지기 만드는거
predictor = dlib.shape_predictor(predictor_file) #랜드마크 검출하는데 사용하는 미리 훈련된 모델 선언

video_capture = cv2.VideoCapture(0) 
g_value_1=[]
g_value_2=[]
g_value_3=[]
base_value_1 = 0.1
base_value_3 = 0.1
count=0
eye_count=0
while (1):
    # 비디오 프레임 읽기
    ret, frame = video_capture.read()

    # 프레임을 회색조로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    face = detector(gray)
    
    #검출 영역 3개의 x,y 값 저장하는 리스트
    sel=[None,None]
    sel2=[None,None]
    sel3=[None,None]
    
    #눈꺼풀 사이의 거리 계산하기 위한 리스트
    eye1=[None,None] #윗눈
    eye2=[None,None] #아랫눈
    
    #눈 감은 상태의 프레임 측정하여 눈 계속 감고 있는지 확인하는 변수
    if face:
        #얼굴 정규화 하는 코드
        (x, y, w, h) = (face[0].left(), face[0].top(), face[0].width(), face[0].height())
        face_img = frame[y:y + h, x:x + w]
        face_img_resized = cv2.resize(face_img, fixed_size, interpolation=cv2.INTER_AREA)
        frame = face_img_resized
        
        #크기 고정한 얼굴로 다시 랜드마크 검출
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        
        #검출한 랜드마크로 값 추출 시작
        if faces:
            count+=1
            if(count<450):
                face = faces[0]
                
                points = np.matrix([[p.x, p.y] for p in predictor(gray, face).parts()]) #이미지에서 검출한 랜드마크 좌표를 2*n 행렬로 저장하는거
                show_parts = points[ALL] #points 복사
                for (i, point) in enumerate(show_parts):
                    x = point[0,0] 
                    y = point[0,1]
                    Fframe = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
                    cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)
                    cv2.putText(frame, "{}".format(i), (x, y - 2),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1) #0.3은 폰트 크기, 뒤부터 색상, 글자 두께
                    if i==43:
                        eye1=(x,y)
                    if i==47:
                        eye2=(x,y)
                        
                        #print(f"눈 1 x y  {eye1[0]}  {eye1[1]}")
                        # eye_gap = eye1[1]-eye2[1]
                        # print(eye_gap)
                        #print(f"눈 2 x y  {eye2[0]}  {eye2[1]}")
                        
                        print(f"눈 간격 {eye2[1]-eye1[1]}")
                        
                    if i==2: #광대
                        sel[0]=(x,y)
                    if i==31: #왼쪽 뺨 검출
                        sel[1]=(int((sel[0][0]+x)/2),int((sel[0][1]+y)/2)) #왼쪽 뺨 좌표 저장
                        temp=0
                        for j in range (8):
                            cv2.circle(frame, (sel[1][0]+dx[j]*3, (sel[1][1]+dy[j]*3)), 1, (255, 255, 0), -1) #저장한 좌표 기준으로 8방향 점 찍기
                            temp+=Fframe[sel[1][0]+dx[j]*3, sel[1][1]+dy[j]*3][1]
                            cv2.circle(frame, (int(sel[1][0]+dx[j]/2*3), int(sel[1][1]+dy[j]/2*3)), 1, (255, 255, 0), -1)
                            temp+=Fframe[int(sel[1][0]+dx[j]/2*3), int(sel[1][1]+dy[j]/2*3)][1]
                            cv2.circle(frame, (sel[1][0]+dx[j]*4, (sel[1][1]+dy[j]*4)), 1, (255, 255, 0), -1)
                            temp+=Fframe[sel[1][0]+dx[j]*4, sel[1][1]+dy[j]*4][1]
                        cv2.circle(frame, ((sel[1][0]), ((sel[1][1]-2))), 1, (255, 255, 0), -1) #가운데 점 찍기
                        temp+=Fframe[sel[1][0], sel[1][1]][1]
                        temp/=25 #평균 내기
                        g_value_1.append(temp)
                        #print(temp)

                    if i==8: #얼굴 아래
                        sel3[0]=(x,y)
                    if i==57: #턱 검출
                        sel3[1]=(int((sel3[0][0]+x)/2),int((sel3[0][1]+y)/2))
                        temp=0
                        for j in range (8):
                            cv2.circle(frame, (sel3[1][0]+dx[j]*3, (sel3[1][1]+dy[j]*3)), 1, (255, 255, 0), -1)
                            temp += Fframe[sel3[1][0]+dx[j]*3, sel3[1][1]+dy[j]*3, 1]
                            cv2.circle(frame, (sel3[1][0]+dx[j]*2, (sel3[1][1]+dy[j]*2)), 1, (255, 255, 0), -1)
                            temp += Fframe[sel3[1][0]+dx[j]*2, sel3[1][1]+dy[j]*2, 1]
                            cv2.circle(frame, (sel3[1][0]+dx[j]*4, (sel3[1][1]+dy[j]*4)), 1, (255, 255, 0), -1)
                            temp += Fframe[sel3[1][0]+dx[j]*4, sel3[1][1]+dy[j]*4, 1]
                        cv2.circle(frame, ((sel3[1][0]), ((sel3[1][1]-2))), 1, (255, 255, 0), -1)
                        temp += Fframe[sel3[1][0], sel3[1][1], 1]
                        temp/=25
                        g_value_3.append(temp)
                        #print(temp)
                print(count)
                    
            if faces:
                if(count>=450):
                    face = faces[0]
                    
                    points = np.matrix([[p.x, p.y] for p in predictor(gray, face).parts()]) #이미지에서 검출한 랜드마크 좌표를 2*n 행렬로 저장하는거
                    show_parts = points[ALL] #points 복사
                    for (i, point) in enumerate(show_parts):
                        x = point[0,0] 
                        y = point[0,1]
                        Fframe = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
                        cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)
                        cv2.putText(frame, "{}".format(i), (x, y - 2),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1) #0.3은 폰트 크기, 뒤부터 색상, 글자 두께
                        
                        if i==43:
                            eye1=(x,y)
                        if i==47:
                            eye2=(x,y)
                            
                            #print(f"눈 1 x y  {eye1[0]}  {eye1[1]}")
                            eye_gap = eye2[1]-eye1[1]
                            # print(eye_gap)
                            #print(f"눈 2 x y  {eye2[0]}  {eye2[1]}")
                            
                        
                            print(f"눈 간격 {eye_gap}")
                            if(eye_gap<=17):
                                eye_count+=1
                            else:
                                eye_count=0
                            
                        if i==2: #광대
                            sel[0]=(x,y)
                        if i==31: #왼쪽 뺨 검출
                            sel[1]=(int((sel[0][0]+x)/2),int((sel[0][1]+y)/2)) #왼쪽 뺨 좌표 저장
                            temp=0
                            for j in range (8):
                                cv2.circle(frame, (sel[1][0]+dx[j]*3, (sel[1][1]+dy[j]*3)), 1, (255, 255, 0), -1) #저장한 좌표 기준으로 8방향 점 찍기
                                temp+=Fframe[sel[1][0]+dx[j]*3, sel[1][1]+dy[j]*3][1]
                                cv2.circle(frame, (int(sel[1][0]+dx[j]/2*3), int(sel[1][1]+dy[j]/2*3)), 1, (255, 255, 0), -1)
                                temp+=Fframe[int(sel[1][0]+dx[j]/2*3), int(sel[1][1]+dy[j]/2*3)][1]
                                cv2.circle(frame, (sel[1][0]+dx[j]*4, (sel[1][1]+dy[j]*4)), 1, (255, 255, 0), -1)
                                temp+=Fframe[sel[1][0]+dx[j]*4, sel[1][1]+dy[j]*4][1]
                            cv2.circle(frame, ((sel[1][0]), ((sel[1][1]-2))), 1, (255, 255, 0), -1) #가운데 점 찍기
                            temp+=Fframe[sel[1][0], sel[1][1]][1]
                            temp/=25 #평균 내기
                            g_value_1.pop(0)
                            g_value_1.append(temp)
                            #print(temp)

                        if i==8: #얼굴 아래
                            sel3[0]=(x,y)
                        if i==57: #턱 검출
                            sel3[1]=(int((sel3[0][0]+x)/2),int((sel3[0][1]+y)/2))
                            temp=0
                            for j in range (8):
                                cv2.circle(frame, (sel3[1][0]+dx[j]*3, (sel3[1][1]+dy[j]*3)), 1, (255, 255, 0), -1)
                                temp += Fframe[sel3[1][0]+dx[j]*3, sel3[1][1]+dy[j]*3, 1]
                                cv2.circle(frame, (sel3[1][0]+dx[j]*2, (sel3[1][1]+dy[j]*2)), 1, (255, 255, 0), -1)
                                temp += Fframe[sel3[1][0]+dx[j]*2, sel3[1][1]+dy[j]*2, 1]
                                cv2.circle(frame, (sel3[1][0]+dx[j]*4, (sel3[1][1]+dy[j]*4)), 1, (255, 255, 0), -1)
                                temp += Fframe[sel3[1][0]+dx[j]*4, sel3[1][1]+dy[j]*4, 1]
                            cv2.circle(frame, ((sel3[1][0]), ((sel3[1][1]-2))), 1, (255, 255, 0), -1)
                            temp += Fframe[sel3[1][0], sel3[1][1], 1]
                            temp/=25
                            g_value_3.pop(0)
                            g_value_3.append(temp)
                            #print(temp)
                    fft_g_value_1 = np.fft.fft(g_value_1)
                    fft_g_value_3 = np.fft.fft(g_value_3)        
                    #FFT 수행한 데이터 길이
                    n = len(g_value_1)

                    #FFT에서 생성되는 주파수
                    freq = np.fft.fftfreq(n)

                    mask = (freq >= 0.022335) & (freq <= 0.111335)

                    fft1_mac = fft_g_value_1[mask]
                    fft3_mac = fft_g_value_3[mask]

                    ifft1 = np.fft.ifft(fft1_mac)
                    ifft3 = np.fft.ifft(fft3_mac)

                    peaks1, _ = find_peaks(ifft1.real, height=-15,distance=3.5,prominence=0.3)  # height는 피크로 인정할 최소 높이를 지정합니다.
                    peaks3, _ = find_peaks(ifft3.real, height=-15,distance=3.5,prominence=0.3)
                    
                    RR1=(60*7)/np.mean(np.diff(peaks1))
                    RR3=(60*7)/np.mean(np.diff(peaks3))
                    if(count==450):
                        base_value_1 = RR1
                        base_value_3 = RR3
                    print("맥박맥박맥박맥박")
                    print(RR1)
                    print(RR3)
                    print("\n")

                        
                    
                
        
    
    cv2.imshow('Video', frame)
        
    # 종료 키 입력 감지
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(f"눈 체크 {eye_count}")
    if (eye_count>20):
        break

play_audio(audio_file)

imgfile = cv2.imread(image_file)
img_rgb = cv2.cvtColor(imgfile, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('sleep!')
plt.axis('off')  # 축을 표시하지 않음
plt.show()
    

