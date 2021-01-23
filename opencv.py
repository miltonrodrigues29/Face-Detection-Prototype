import cv2

img=cv2.imread("new1.jpg",1)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.imshow("Astronaut",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows();

# import glob
# images=glob.glob("*.jpg")
# for image in images:
#     img=cv2.imread(image,0)
#     re=cv2.resize(img,(100,100))
#     cv2.imshow("hey",re)
#     cv2.waitKey(500)
#     cv2.destroyAllWindows()
#     cv2.imwrite("resized"+image,re)