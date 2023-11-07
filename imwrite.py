import cv2  
# read image  
img = cv2.imread('dog.jpg', 1)  
# save image  
status = cv2.imwrite('dog-write.jpg',img)  
print("Image written sucess? : ", status)  