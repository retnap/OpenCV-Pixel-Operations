import cv2
import numpy as np 
import matplotlib.pyplot as plt 


path = "....test_image_path..."
img = cv2.imread(path)

print(img.shape) 
#height, width, channel of picture
#Channel: 3 --> Color
#Channel: 1 --> Grayscale 

print("height: {} pixels".format(img.shape[0]))
print("width: {} pixels".format(img.shape[1]))
print("channel: {} pixels".format(img.shape[2]))
print("Image Size: {}".format(img.size))
print("Data Type: {}".format(img.dtype))


cv2.imshow("Terim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()