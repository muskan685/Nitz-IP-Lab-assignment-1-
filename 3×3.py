import numpy as np
import cv2
import matplotlib.pyplot as plt

binary_image = np.zeros((100,100), dtype=np.uint8)
binary_image[40:70, 40:70] = 255

for _ in range(100):
    x, y = np.random.randint(0,100,2)
    binary_image[x,y] = 255

kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(binary_image, kernel, iterations=1)

plt.subplot(1,2,1)
plt.title("Noisy")
plt.imshow(binary_image, cmap='gray')
plt.subplot(1,2,2)
plt.title("Noise free")
plt.imshow(eroded, cmap='gray')
plt.show()
