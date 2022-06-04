import matplotlib.pyplot as plt
import numpy as np
import cv2

# 读取图片，设置中文
plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/1.2.jpg')
plt.subplot(221), plt.title("1.原图"), plt.axis('off')
plt.imshow(img, cmap="gray")

# 统计下像素值
# 利用np初始化数组
bar = np.zeros(256, dtype=int)
for i in img:
    for j in i:
        bar[j] += 1

# 找到像素分布的范围
# flag=0
# for j,i in enumerate(bar):
#     if i!=0 and flag==0:
#         print(j)
#         flag=1
#     if i==0 and flag==1:
#         print(j)
#         break

# 选择的点a(50,25),点b(125,225)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] <= 80:
            img[i][j] *= 0.3125
        elif img[i][j] <= 125:
            img[i][j] = 40 * (img[i][j] - 80)/9 + 25
        else:
            img[i][j] = (img[i][j] - 125) * 3 / 13 + 225
plt.subplot(223), plt.plot(bar), plt.title('原始直方图')
bar = np.zeros(256, dtype=int)
for i in img:
    for j in i:
        bar[j] += 1
plt.subplot(224), plt.plot(bar), plt.title('线性展宽后的直方图')
plt.subplot(222), plt.title("2.线性展宽后"), plt.axis('off')
plt.imshow(img, cmap="gray")
plt.show()
