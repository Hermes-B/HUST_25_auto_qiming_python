#此为opencv相关基本介绍的第一篇
#观前须知（）；
#1.需先安装opencv库，numpy库
#2.建议有一定python语法基础（没有其实也没关系，大部分很好懂）
#3.一边学一边规划一边写的，逻辑可能比较混乱，请多谅解
#4.顺序：imagebasic-numpy-pixel-...
#5.使用方式：每段整段取消注释调试使用（可能需要手动加上最后的几行） 
#快捷键：选中需要注释的部分ctrl+“/”（右shift左侧按键） 取消同理
#6.后续（可能）继续更新，敬请期待（


import cv2 as cv
import numpy as np
image=cv.imread("test.png",1)#内为(文件路径，输出模式（默认1彩色，0黑白（灰度模式）)，存储为image变量
# #灰度：由0（纯黑）-255（纯白）表示
# #实际上以数组形式存储了像素点
# print(image)#会打印图片相关部分像素值




# #图像属性
# #shape:
# #彩色：数组（垂直像素，水平像素，通道数）
# #灰色：数组（垂直像素，水平像素）
# #size：
# #像素个数=垂直像素*水平像素*通道数（灰色图通道数为1）
# #dtype:
# #图像数据类型

# print(image.shape,image.size,image.dtype)

# #以当前测试图片为例
# #灰色结果为：((1440, 2560) 3686400 uint8)
# #彩色结果为：((1440, 2560, 3) 11059200 uint8)

# px=image[720,1280]#(以image[y,x]表示某个像素点)
# print(px)#若为彩色，打印该像素BGR值；若为黑白，打印该像素灰度值
# #BGR值：代表蓝、绿、红 3个通道 每个值范围为(0-255)

# #分别获取BGR的值，仅在彩色模式下可用
# blue=image[720,1280,0]
# green=image[720,1280,1]
# red=image[720,1280,2]
# print(blue,green,red)


# px=[255,255,255]#修改该像素BGR值
# #当BGR三个值相同时，即得灰度图像，与0-255灰度相同

# #把某一区域变为纯白
# for i in range(500,1000):
#     for j in range(1200,1800):
#         image[i,j]=(255,255,255)

# #将BGR转为灰度
# imggray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# #转为灰度后，BGR三个通道变为一个灰度通道，无法再恢复BGR通道

# #转为HSV色彩空间
# # H(色调 0-180 以赤橙黄绿青蓝紫顺序排列)
# # S(饱和度 0-255 色彩深浅)
# # V(明度 0-255 图像明暗)
# hsv_image=cv.cvtColor(image,cv.COLOR_BGR2HSV)
# #HSV后续识别处理特定颜色时常用

# #图像拆分
# b,g,r=cv.split(image)
# #拆分后呈现每个通道的灰度图（即各像素BGR值为(b,b,b),(g,g,g),(r,r,r)的图像）
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# #图像合并
# bgr=cv.merge([b,g,r])
# #合并后恢复为原图像
# cv.imshow("bgr",bgr)
# #hsv通道拆分合并方法相同

# #拆分合并方法可用于单独处理某一通道值（也可直接通过数组操作处理）
# #如将图像的红色通道值全部设为0
# r[:,:]=0
# image=cv.merge([b,g,r]) 
# #合并后红色通道值全部为0
# cv.imshow("image",image)
# #或直接处理
# image[:,:,2]=0
# cv.imshow("image",image)

# #Alpha通道（透明度通道）
# #Alpha通道：表示图像透明度的通道，0-完全透明，255-完全不透明
# #在OpenCV中，图像通常是BGR格式的，Alpha通道可以通过添加一个额外的通道来实现
# bgra=cv.imread("test.png",-1)
# b,g,r,a=cv.split(bgra)
# #拆分后a即为Alpha通道
# a[:,:]=128#将透明度设为128（半透明）
# bgra_128=cv.merge([b,g,r,a])
# cv.imwrite("test_bgra_128.png",bgra_128)#保存为带透明度的png图片
# a[:,:]=255#完全不透明
# bgra_255=cv.merge([b,g,r,a])
# cv.imwrite("test_bgra_255.png",bgra_255)
# a[:,:]=0#完全透明
# bgra_0=cv.merge([b,g,r,a])
# cv.imwrite("test_bgra_0.png",bgra_0)
# #注意：jpg等格式不支持透明度，保存时会自动去除Alpha通道，png等格式支持透明度
# #直接显示图像效果相同，需保存才可看出透明度差异 



cv.imshow("image",image)#分别为(窗口名,要显示的图像)
cv.waitKey(0)#()内为延迟，函数返回值为输入键对应ASCII码,0输入任何键后执行下一步,非0则延迟结束自动关闭
cv.destroyAllWindows()#关闭所有窗口，Waitkey+destroy必须写在代码里，否则无法正常运行

