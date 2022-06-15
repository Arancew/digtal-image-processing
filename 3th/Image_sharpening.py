import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


# 求卷积运算
def convolution(img_old, kernel):
    img_new = np.zeros(img.shape, dtype=int)
    for i in range(1, img_new.shape[0] - 1):  # 第一列和最后一列不用处理
        for j in range(1, img_new.shape[1] - 1):
            tmp = 0  # 初始化为0,用来求和
            for k in range(-1, 2):
                for l in range(-1, 2):
                    tmp += img_old[i + k][j + l] * kernel[k + 1][l + 1]
            img_new[i][j] = abs(tmp)
    return img_new


plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/lena.jpg')  # 读取图片
# img = img[:, :, 0]  # 把图片从三通道变为单通道
plt.subplot(241), plt.title("1.原图"), plt.axis('off')
plt.imshow(img, cmap="gray")

#  水平锐化
kernel_horizontal = np.array([[1, 2, 1],
                              [0, 0, 0],
                              [-1, -2, -1]])
img_horizontal = convolution(img, kernel_horizontal)
plt.subplot(242), plt.title("2.水平锐化后"), plt.axis('off')
plt.imshow(img_horizontal, cmap="gray")
# 垂直锐化

kernel_vertical = np.array([[1, 0, -1],
                            [2, 0, -2],
                            [1, 0, -1]])
img_vertical = convolution(img, kernel_vertical)
plt.subplot(243), plt.title("3.垂直锐化后"), plt.axis('off')
plt.imshow(img_vertical, cmap="gray")
# Roberts锐化
# 公式 g(i,j)=abs(f(i+1,j+1)-f(i,j)+abs(f(i+1,j)-f(i,j+1))
img_Roberts = np.zeros(img.shape, dtype=int)
for i in range(1, img.shape[0] - 1):  # 第一列和最后一列不用处理
    for j in range(1, img.shape[1] - 1):
        img_Roberts[i][j] = abs((int)(img[i + 1][j + 1]) - (int)(img[i][j])) + abs(
            (int)(img[i + 1][j]) - (int)(img[i][j + 1]))
plt.subplot(244), plt.title("4.Roberts锐化后"), plt.axis('off')
plt.imshow(img_Roberts, cmap="gray")

# Sobel锐化
# 利用上面垂直锐化和水平锐化的结果
img_Sobel = np.sqrt(img_vertical * img_vertical + img_horizontal * img_horizontal)
# print(np.max(img_Sobel))
img_Sobel = np.minimum(img_Sobel, 255)  # 调整灰度大小，最大为255
# print(np.max(img_Sobel))
plt.subplot(245), plt.title("5.Sobel锐化后"), plt.axis('off')
plt.imshow(img_Sobel, cmap="gray")

# Laplacian锐化
kernel_Laplacian = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])
img_Laplacian = convolution(img, kernel_Laplacian)
img_Laplacian = abs(img_Laplacian)
plt.subplot(246), plt.title("7.Laplacian锐化后"), plt.axis('off')
plt.imshow(img_Laplacian, cmap="gray")
# 变形Laplacian锐化

kernel_Laplacian1 = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])
img_Laplacian1 = convolution(img, kernel_Laplacian1)
img_Laplacian1 = abs(img_Laplacian1)
plt.subplot(247), plt.title("7.LaplacianH4锐化后"), plt.axis('off')
plt.imshow(img_Laplacian1, cmap="gray")
# Wallis锐化
img_Wallis = np.zeros(img.shape, dtype=int)
for i in range(1, img.shape[0] - 1):  # 第一列和最后一列不用处理
    for j in range(1, img.shape[1] - 1):
        s = np.log(img[i - 1][j] + 1) + np.log(img[i + 1][j] + 1) + np.log(img[i][j - 1] + 1) + np.log(
            img[i][j + 1] + 1)  # 加1防止取0
        s = s*46/4  # 让取值从5.45到255
        img_Wallis[i][j] = (int)(46 * np.log(img[i][j]+1) - s)
img_Wallis=img_Wallis+abs(np.min(img_Wallis))
plt.subplot(248), plt.title("8.Wallis锐化后"), plt.axis('off')
plt.imshow(img_Wallis, cmap="gray")

plt.show()
