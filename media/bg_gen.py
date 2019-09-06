import cv2
import numpy as np

img = np.zeros((600,600),dtype = np.uint8)
img += 255


cv2.line(img,(200,0),(200,600),(0,0,0),20)
cv2.line(img,(400,0),(400,600),(0,0,0),20)
cv2.line(img,(0,200),(600,200),(0,0,0),20)
cv2.line(img,(0,400),(600,400),(0,0,0),20)

cv2.imwrite('background.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
