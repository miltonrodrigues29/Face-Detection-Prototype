import cv2
face_cascade =cv2.CascadeClassifier()
face_cascade.load('haarcascade_frontalface_default.xml')
img=cv2.imread("newimg.jpg")
gray_image =cv2.imread("newimg.jpg",0)
print(type(face_cascade))
faces = face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)
faces = face_cascade.detectMultiScale(gray_image, 1.05, 5)
for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

resized= cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()