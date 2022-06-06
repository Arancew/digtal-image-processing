import matplotlib.pyplot as plt
import numpy as np


plt.rc("font", family='Microsoft YaHei')
img = plt.imread('../img/4.1.jpg')
img=img[:,:,0]*255
plt.subplot(131), plt.title('原始图像')
plt.imshow(img, 'gray')
best_th=1 # 选出来的最好的阈值
best_s=0
bar=[]
for th in range(1,255):#阈值设置为[1,254]
    u1=0
    u1_cnt=0
    u2=0 #计算俩类的灰度值
    u2_cnt=0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j]<th:
                u1+=img[i][j]
                u1_cnt+=1
            else:
                u2+=img[i][j]
                u2_cnt+=1
    if u1_cnt!=0:
        u1/=u1_cnt
    if u2_cnt!=0:
        u2/=u2_cnt
    s=(u2-th)*(th-u1)/(u2-u1)*(u2-u1)
    bar.append(s)
    if s>best_s:
        best_s=s
        best_th=th
img_new=np.zeros(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]<best_th:
            img_new[i][j]=0
        else:
            img_new[i][j]=255
plt.subplot(132), plt.title('图像分割后图像')
plt.imshow(img_new, 'gray')
plt.axis('off')
plt.subplot(133), plt.title('s与th变化趋势')
plt.plot(bar)
plt.show()
