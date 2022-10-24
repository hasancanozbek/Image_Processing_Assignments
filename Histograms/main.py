import numpy as np
import cv2
import matplotlib.pyplot as ml

y_size = 500
x_size = 500
photo = cv2.resize(cv2.imread("photo.jpg", 0), (x_size, y_size))

cv2.imshow("foto", photo)
# cv2.waitKey()

hist = np.zeros(256, dtype=int)
for f in range(x_size):
    for k in range(y_size):
        hist[photo[f, k]] = hist[photo[f, k]] + 1

ml.plot(hist)
ml.show()
