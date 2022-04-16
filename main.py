import numpy as np
from imageio import imread, imwrite
import cv2

img = imread('images/test1.jpg')
arr = img * np.array([0.1, 0.2, 0.5])
arr2 = (255*arr/arr.max()).astype(np.uint8)
imwrite('images/image_out.jpg', arr2)
img2 = cv2.imread('images/image_out.jpg')
gamma = 2
gamma_img = np.array(255*(img2/255)**gamma, dtype=np.uint8)
cv2.imwrite('images/image_out_gamma.jpg', gamma_img)
print("Conversion complete")