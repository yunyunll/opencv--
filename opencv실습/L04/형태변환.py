import cv2 as cv
import sys
from google.colab.patches import cv2_imshow

img = cv.imread('/content/drive/MyDrive/2024년도 1학기/컴퓨터비전/soccer.jpg')

if img is None :
  sys.exit('파일이 존재하지 않습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv2_imshow(img)
cv2_imshow(gray)
cv2_imshow(gray_small)

cv.waitKey()
cv.destroyALLWindows()

print(type(img))
print(img.shape)