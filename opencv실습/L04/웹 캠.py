import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 카메라와 연결 시도
if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    ret, frame = cap.read()  # 비디오에서 프레임을 읽기
    if not ret:
        break  # 프레임 획득 실패 시 루프 종료

    cv.imshow('Video display', frame)  # 비디오 프레임 표시
    key = cv.waitKey(1)  # 1밀리초 동안 키 입력 기다림
    if key == ord('q'):
        break  # 'q' 키를 누르면 루프 종료

cap.release()  # 카메라와의 연결 종료
cv.destroyAllWindows()  # 모든 창 닫기