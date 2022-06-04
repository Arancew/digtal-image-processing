import matplotlib.pyplot as plt

plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/1.1.jpg')  # 读取图片
plt.subplot(121),plt.title("1.原图"), plt.axis('off')
plt.imshow(img, cmap="gray")
# print(img.shape)
new_img = 255 - img
plt.subplot(122),plt.title("2.灰度值反转后"), plt.axis('off')
plt.imshow(new_img, cmap="gray")
plt.show()
