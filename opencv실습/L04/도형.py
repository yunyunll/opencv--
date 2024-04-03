import cv2 as cv
import sys
from google.colab.patches import cv2_imshow

img = cv.imread('/content/drive/MyDrive/2024년도 1학기/컴퓨터비전/soccer.jpg')

if img is None :
  sys.exit('파일이 존재하지 않습니다.')

cv.rectangle(img,(290,780),(620,950),(0,0,255),2)
cv.putText(img,'mouse',(290,770),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2_imshow(img)

cv.waitKey()
cv.destroyALLWindows()

print(type(img))
print(img.shape)