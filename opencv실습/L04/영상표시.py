import cv2 as cv
import sys
from google.colab.patches import cv2_imshow


img = cv.imread('/content/drive/MyDrive/2024년도 1학기/컴퓨터비전/soccer.jpg')

if img is None :
  sys.exit('파일이 존재하지 않습니다.')

cv2_imshow(img)
print(img[0,0,0],img[0,0,1],img[0,0,2])

cv.waitKey()
cv.destroyALLWindows()

print(type(img))
print(img.shape)