#Melike Ekinci 02205076061

import cv2
import numpy as np
#resmi alıp gösterir
resim2 = cv2.imread('omer.jpg')
cv2.imshow('resim', resim2)
#işlenicek resim
resim = cv2.imread('omer.jpg',0)
cv2.imshow('resim-0', resim)
#resmi terse çevirir
[h, w] = resim.shape
resim2 = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        resim2[i, j] = 255 - resim[i, j]
#resmi gösterir
cv2.imshow("Ters resim", resim2)
cv2.waitKey()