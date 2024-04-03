import cv2
import sys
from google.colab.patches import cv2_imshow

BrushSize = 5
LColor, RColor = (255, 0, 0), (0, 0, 255)

def painting(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), BrushSize, LColor, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), BrushSize, RColor, -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), BrushSize, LColor, -1)
    elif event == cv2.EVENT_RBUTTONDOWN and flags == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img, (x, y), BrushSize, LColor, -1)
    
    cv2_imshow(img)

img = cv2.imread('/content/drive/MyDrive/2024년도 1학기/컴퓨터비전/soccer.jpg')

cv2.namedWindow('Painting')
cv2_imshow(img)
cv2.setMouseCallback('Painting', painting)

while True:
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break