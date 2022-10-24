import numpy as np
import cv2
import matplotlib.pyplot as ml

y_boyut = 500
x_boyut = 500
foto = cv2.resize(cv2.imread("photo.jpg", 0), (x_boyut, y_boyut))

cv2.imshow("foto", foto)
# cv2.waitKey()

hist = np.zeros(256, dtype=int)
for f in range(x_boyut):
    for k in range(y_boyut):
        hist[foto[f, k]] = hist[foto[f, k]] + 1

ml.plot(hist)
ml.show()
