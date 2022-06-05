import cv2
import matplotlib.pyplot as plt
import numpy
import skimage

plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/2.1.jpg')

plt.subplot(221), plt.title('原始图像')
plt.imshow(img, 'gray')
noise_img = skimage.util.random_noise(img, mode='salt')*255
plt.subplot(222), plt.title('椒盐噪声图像')
plt.imshow(noise_img, 'gray')
# 均值滤波

mean_img = noise_img

for i in range(1, noise_img.shape[0] - 1):  # 第一列和最后一列用不到
    for j in range(1, noise_img.shape[1] - 1):  # 第一行和最后一行用不到
        tmp = 0  # 用来求和
        for k in range(-1, 2):
            for l in range(-1, 2):
                tmp += noise_img[i + k][j + l]
        mean_img[i][j] = tmp / 9
plt.subplot(223), plt.title('均值滤波后图像')
plt.imshow(mean_img, 'gray')

# 中值滤波
median_img = noise_img

for i in range(1, noise_img.shape[0] - 1):  # 第一列和最后一列用不到
    for j in range(1, noise_img.shape[1] - 1):  # 第一行和最后一行用不到
        tmpp = []  # 用来记录9个值
        for k in range(-1, 2):
            for l in range(-1, 2):
                tmpp.append(noise_img[i + k][j + l])
        list.sort(tmpp)
        median_img[i][j] = tmpp[4]  # 取得中值

plt.subplot(224), plt.title('中值滤波后图像')
plt.imshow(median_img, 'gray')
plt.show()
