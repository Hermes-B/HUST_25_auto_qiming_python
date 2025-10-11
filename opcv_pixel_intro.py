import cv2 as cv
import numpy as np

#后续需了解numpy后方可理解

#创建纯色图
width=2000
height=1000
#决定二维数组大小，即图片大小
img1=np.zeros((height,width),np.uint8) #创建二维全0数组，即纯黑图
img2=np.ones((height,width),np.uint8)*255 #创建全255数组，即纯白图
cv.imshow("img",img2)
cv.waitKey(0)
cv.destroyAllWindows()

#改背景
width=2000
height=1000
img=np.zeros((height,width),np.uint8)#以纯黑图为背景
img[250:750,500:1500]=255#修改中间部分为白色
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()

#画间隔白色块
width=2000
height=1000
img=np.zeros((height,width),np.uint8)#以纯黑图为背景
for i in range(0,width,200):
    img[:,i:i+100]=255#将间隔改为白色
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()

#创建彩色图像
width=2000
height=1000
img=np.zeros((height,width,3),np.uint8)#以纯黑图为背景
blue=img.copy()
blue[:,:,0]=255#创建通道0为255，其他2个为0的纯蓝图像，下面两操作同理
green=img.copy()
green[:,:,1]=255
red=img.copy()
red[:,:,2]=255
cv.imshow("img1",blue)
cv.imshow("img2",green)
cv.imshow("img3",red)
cv.waitKey(0)
cv.destroyAllWindows()

#创建随机(噪音)图像
width=2000
height=1000 
img1=np.random.randint(256,size=(height,width),dtype=np.uint8)
#每个点取0-255随机值的灰度图
img2=np.random.randint(256,size=(height,width,3),dtype=np.uint8)
#每个点BGR取随机值的彩色图
cv.imshow("img1",img1)#结果为雪花图
cv.imshow("img2",img2)
cv.waitKey(0)
cv.destroyAllWindows()

#拼接图像
width=1000
height=500
img1=np.zeros((height,width),np.uint8)
img2=np.ones((height,width),np.uint8)*255
hsimg=np.hstack((img1,img2))
#hstack:将元组(数组1，数组2...)水平拼接到一起（数组大小要求完全一样）
#！！外面有一个函数括号，内部为元组括号，表现为两层括号
vsimg=np.vstack((img1,img2))
#vstack:其他同理，为垂直拼接
cv.imshow("hsimg",hsimg)
cv.imshow("vsimg",vsimg)
cv.waitKey(0)
cv.destroyAllWindows()

