import cv2
import numpy as np
x = 0
y = 44
w = 2880
h = 750

img1= cv2.imread("01.png")
crop_image1 = img1[y:y+h, x:x+w]
img2= cv2.imread("02.png")
crop_image2 = img2[y:y+h, x:x+w]
img3= cv2.imread("03.png")
crop_image3 = img3[y:y+h, x:x+w]
img4= cv2.imread("04.png")
crop_image4 = img4[y:y+h, x:x+w]
img5= cv2.imread("05.png")
crop_image5 = img5[y:y+h, x:x+w]
img6= cv2.imread("06.png")
crop_image6 = img6[y:y+h, x:x+w]
img7= cv2.imread("07.png")
crop_image7 = img7[y:y+h, x:x+w]
img8= cv2.imread("08.png")
crop_image8 = img8[y:y+h, x:x+w]
img9= cv2.imread("09.png")
crop_image9 = img9[y:y+h, x:x+w]
img10= cv2.imread("010.png")
crop_image10 = img10[y:y+h, x:x+w]
img11= cv2.imread("011.png")
crop_image11 = img11[y:y+h, x:x+w]
img12= cv2.imread("012.png")
crop_image12 = img12[y:y+h, x:x+w]
img13= cv2.imread("013.png")
crop_image13 = img13[y:y+h, x:x+w]
img14= cv2.imread("014.png")
crop_image14 = img14[y:y+h, x:x+w]
img15= cv2.imread("015.png")
crop_image15 = img15[y:y+h, x:x+w]
img16= cv2.imread("016.png")
crop_image16 = img16[y:y+h, x:x+w]
combine_photo = np.vstack((crop_image1, crop_image2, crop_image3, crop_image4, crop_image5, crop_image6, crop_image7, crop_image8, crop_image9, crop_image10, crop_image11, crop_image12, crop_image13, crop_image14, crop_image15, crop_image16))
cv2.imwrite('combine_photo.png', combine_photo)