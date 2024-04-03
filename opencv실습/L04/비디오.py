import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 카메라와 연결 시도
if not cap.isOpened():
    sys.exit('카메라 연결 실패')

frames = []
while True:
    ret, frame = cap.read()
    # 비디오를 구성하는 프레임 획득
    if not ret:
        break
    print('프레임 획득에 실패하여 루프를 나갑니다.')
    cv.imshow('Video display', frame)
    key = cv.waitKey(1)
    if key == ord('c'):
        # frames에 프레임 추가
        frames.append(frame)
        # 1밀리초 동안 키보드 입력 기다림
        # 키가 들어오면 프레임을 리스트에 추가
    elif key == ord('q'):
        # 'q' 키가 들어오면 루프를 빠져나감
        break

cap.release()
cv.destroyAllWindows()

# 수집된 영상이 있을 경우
if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))
    cv.imshow('collected images', imgs)
    cv.waitKey()
    cv.destroyAllWindows()

print(len(frames))
print(frames[0].shape)
print(type(imgs))
print(imgs.shape)