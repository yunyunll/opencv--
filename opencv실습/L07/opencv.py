import cv2 as cv
import numpy as np

# Image initialization
img = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0]], dtype=np.float32)

# Kernel initialization
ux = np.array([[-1,0,1]])
uy = np.array([[-1],[0],[1]])

# Gaussian Kernel
k = cv.getGaussianKernel(3,1)
g = np.outer(k, k.transpose())

# Filtering
dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux)
dyy = dy * dy
dxx = dx * dx
dyx = dy * dx

gdyy = cv.filter2D(dyy, cv.CV_32F, g)
gdxx = cv.filter2D(dxx, cv.CV_32F, g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)

C = (gdyy * gdxx - gdyx * gdyx) - 0.04 * (gdyy + gdxx) * (gdyy + gdxx)

# Printing
np.set_printoptions(precision=2)
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C)
print(img)

# Displaying the image
popping = np.zeros([160, 160], np.uint8)
for j in range(0, img.shape[0]):
    for i in range(0, img.shape[1]):
        popping[j, i] = np.uint8((C[j // 16, i // 16] + 0.06) * 700)

cv.imshow('Image Display2', popping)
cv.waitKey(0)
cv.destroyAllWindows()
