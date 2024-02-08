import cv2
import numpy as np

path = "....test_image_path...."

img = cv2.imread(path)
#print(img)

#resimdeki herhangi bir koordinata erismek
px = img[0,0]  #0,0 'daki piksel degerlerini dondurur
print(px) 


(b, g, r) = img[50, 30]
print("(0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))
#50,30 daki rgb renk degerleri

"""
-->Bir goruntudeki renkler RGB'nin karisimdan olusmussa 
0 ile 255 arasinda degerler alir.
B: 0-255
G: 0-255
R: 0-255

0 - Black
255 - White 

0'a yaklastikca siyahlasir ve 255'e yaklastikca beyazlasir

"""

#rgb 'ye tek tek erismek
blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]

print("---------------------------------------")

#img[100,100] un degerlerini degistirmek
print("Before:", img[100,100])
img[100,100] = [100,100,100]
print("After:", img[100,100])


print("---------------------------------------")

#rgb degerlerine tek tek erismek - 2
print("RED VALUE:", img.item(10,10,2)) #BGR olarak Red indeks degeri 2


img.itemset((10, 10, 2), 100) #red degerine erismek ve 100 ile degistirmek
print("After Red Value:", img.item(10,10,2))
