import cv2
import numpy as np

#event=[i for i in dir(cv2) if 'EVENT'in i]
#print(event)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,230,19),5)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:

        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strxy = str(x) + ',' + str(y)
        cv2.putText(img, strxy, (x, y), font, .5, (255, 255, 13), 2)
        cv2.imshow('image', img)
        #BGR CHANNELS


#img=np.zeros((500,512,3),np.uint8)
#THIS IS FOR BLACK IMAGES
img=cv2.imread('kri.jpg')
#picture from my own collectios
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
