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

# 找到像素分布的范围和点a,b
flag = 0
ax = 0
ay = 0
bx = 0
by = 0
for j, i in enumerate(bar):
    if i != 0 and flag == 0:
        ax = j
        ay = i
        flag = 1
    if i == 0 and flag == 1:
        bx = j
        by = i
        break

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] <= ax:
            img[i][j] = 0
        elif img[i][j] <= bx:
            img[i][j] = (by - ay) / (bx - ax) * (img[i][j] - ax) + ay
        else:
            img[i][j] = 0
plt.subplot(223), plt.bar(range(len(bar)),bar), plt.title('原始直方图')
bar = np.zeros(256, dtype=int)
for i in img:
    for j in i:
        bar[j] += 1
plt.subplot(224), plt.bar(range(len(bar)),bar), plt.title('灰度窗后的直方图')
plt.subplot(222), plt.title("2.灰度窗后"), plt.axis('off')
plt.imshow(img, cmap="gray")
plt.show()
