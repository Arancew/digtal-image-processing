import matplotlib.pyplot as plt
import numpy as np

# 读取图片，设置中文
plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/1.3.jpg')
plt.subplot(121), plt.title("1.原图"), plt.axis('off')
plt.imshow(img)
# print(img.shape[:2])  #获取像素的行数和列数
new_img = np.ones(img.shape[:2], dtype=int)


# Y= R*0.299+G*0.587+B*0.114,获得新图
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        new_img[i][j] = img[i][j][0] * 0.299 + img[i][j][1] * 0.587 + img[i][j][2] * 0.114
plt.subplot(122), plt.title("2.转化为灰度值后"), plt.axis('off')
plt.imshow(new_img, cmap="gray")
plt.show()
