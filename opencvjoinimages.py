import cv2
import numpy as np
img=cv2.imread('kri.jpg')
img2=cv2.imread('ass.JPG')

print(img.shape)#return a tuple of number of rows,coloums,and channels
print(img.size)#return total number of pixels is accessed
print(img.dtype)#returns image datatype is obtained
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
#ball=img[50:90,78:60]
#Img[27:33, 34:23]=ball

#resize images:
img=cv2.resize(img,(1000,900))
img2=cv2.resize(img2,(1000,900))
test=cv2.add(img,img2);

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

