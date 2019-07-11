import cv2
img=cv2.imread('kri.jpg',1)
img=cv2.line(img,(0,0),(200,300),(255,0,0),5)
img=cv2.arrowedLine(img,(20,20),(200,300),(147,96,44),6,)

img=cv2.rectangle(img,(10,10),(300,200),(123,22,34),-1)

img=cv2.circle(img,(10,200),10,(100,20,40),10)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'open cv',(500,600),font,6,(0,0,56),5,cv2.LINE_AA)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()