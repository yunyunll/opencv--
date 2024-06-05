import numpy as np
import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt
import pygame

model=tf.keras.models.load_model('dmlp_trained.h5')

def reset():
    global recognition

    recognition= np.ones((200, 520, 3), dtype=np.uint8) * 255
    for i in range(5):
        cv.rectangle(recognition, (10 + i * 100, 50), (10 + (i + 1) * 100, 150), (0, 0, 255))
    cv.putText(recognition, 'e:erase s:show r:recognition q:quit', (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1)

def grab_numerals():
    numerals=[]
    for i in range(5):
        roi= recognition[51:149, 11 + i * 100:9 + (i + 1) * 100, 0]
        roi=255-cv.resize(roi,(28,28),interpolation=cv.INTER_CUBIC)
        numerals.append(roi)
    numerals=np.array(numerals)
    return numerals

def show():
    numerals=grab_numerals()
    plt.figure(figsize=(25,5))
    for i in range(5):
        plt.subplot(1,5,i+1)
        plt.imshow(numerals[i],cmap='gray')
        plt.xticks([]); plt.yticks([])
    plt.show()

def recognition():
    numerals=grab_numerals()
    numerals=numerals.reshape(5,784)
    numerals=numerals.astype(np.float32)/255.0
    res=model.predict(numerals)
    class_id=np.argmax(res,axis=1)
    for i in range(5):
        cv.putText(recognition, str(class_id[i]), (50 + i * 100, 180), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    pygame.Beep(1000,500)
BrushSiz=4
LColor=(0,0,0)

def writing(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(recognition, (x, y), BrushSiz, LColor, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(recognition, (x, y), BrushSiz, LColor, -1)

reset()
cv.namedWindow('Writing')
cv.setMouseCallback('Writing',writing)

while(True):
        cv.imshow('Writing', recognition)
        key=cv.waitKey(1)
        if key==ord('e'):
            reset()
        elif key==ord('s'):
            show()
        elif key==ord('r'):
            recognition()
        elif key==ord('q'):
            break

cv.destroyAllWindows()