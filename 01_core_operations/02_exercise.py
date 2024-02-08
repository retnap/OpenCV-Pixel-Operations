import cv2 
import numpy as np 

import matplotlib.pyplot as plt 


path = "....test_image_path...."
img = cv2.imread(path)
#print(img)

#Goruntunun belli bir piksel bolgesini tarama
corner = img[0:100,0:100] #ilk deger y eksenini tarar, diger eksen x eksenini tarar

#Goruntunun belli bolgesini tarama ve piksel degerlerini degistirme
img[0:200, 0:250] = (255, 0, 0) #BGR sirasi ile degerler yaziliyor

cv2.imshow("Muslera", img)
cv2.imshow("Corner", corner)
cv2.imshow("Corner-2", img)

cv2.waitKey(0)
cv2.destroyAllWindows()