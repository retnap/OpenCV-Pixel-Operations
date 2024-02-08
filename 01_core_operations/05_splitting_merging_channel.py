import cv2
import numpy as np
import matplotlib.pyplot as plt


path = "....test_image_path..."
img = cv2.imread(path)
print("Shape: {}".format(img.shape))

(B, G, R) = cv2.split(img) #resim icerisindeki kirmizi mavi ve yesil i alip ayri ayri depoluyor
merged = cv2.merge([B, G, R])  #ayrilan B G R yi birlestirerek gosterdi


black = np.zeros(img.shape[:2], dtype="uint8")
#np.zeros ile bana orijinal resmin seklinde siyah bir matris dondurdu
#cv2.imshow("Black", black)


cv2.imshow("Red", cv2.merge([black, black, R]))
#Birlestirilmis resimde (BGR) ilk iki deger siyah ve Red degerini yukarida
#tanimladigin sekilde goster 

cv2.imshow("Green", cv2.merge([black, G, black]))

cv2.imshow("Red", cv2.merge([B, black, black]))


# cv2.imshow("Icardi", img)

# cv2.imshow("Icardi - merged", merged)

# cv2.imshow("Icardi-B", B) #B G R yi tek tek ayirarak gosterdi
# cv2.imshow("Icardi-G", G)
# cv2.imshow("Icardi-R", R)


cv2.waitKey(0)
cv2.destroyAllWindows()

