import matplotlib.pyplot as plt
import numpy as np
import cv2

# 读取图片，设置中文
plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/1.2.jpg')
plt.subplot(121), plt.title("1.原图"), plt.axis('off')
plt.imshow(img,cmap="gray")



new_img=cv2.equalizeHist(img)
plt.subplot(122), plt.title("2.直方图均衡化后"), plt.axis('off')
plt.imshow(new_img, cmap="gray")
plt.show()
