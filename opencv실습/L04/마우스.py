import cv2 as cv
import sys
from google.colab.patches import cv2_imshow

img = cv.imread('/content/drive/MyDrive/2024년도 1학기/컴퓨터비전/soccer.jpg')

if img is None :
  sys.exit('파일이 존재하지 않습니다.')

def draw(event,x,y,flags,param):
  if event==cv.EVENT_LBUTTONDOWN:
      cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2)
  elif event==cv.EVENT_RBUTTONDOWN:
      cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),2)

  cv2_imshow(img)

cv.namedWindow('Drawing')
cv.setMouseCallback('Drawing',draw)


while(True):
  if cv.waitKey(1)==ord('q'):
      cv.destroyAllWindows()
      break