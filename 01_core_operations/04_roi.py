import cv2
import numpy as np
import matplotlib.pyplot as plt

# ROI: region of interest --> ilgi alani
#Goruntulerde ilgilenilen bazi ozel alanlar, yuzleri bulmak gibi

path = "....test_image_path..."
img = cv2.imread(path)
print("Shape: {}".format(img.shape))


roi = img[0:200, 350:600] #Hedefin yuzu tespit edildi
img[0:50, 400:500] = roi  #Kesilen bolgeyi resim uzerinde baska bir yere yapistirmak


cv2.imshow("Icardi", img)
cv2.imshow("Roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

