import cv2
import numpy as np
a,b=map(int,input("请输入左上角坐标:").split(","))
c,d=map(int,input("请输入右下角坐标:").split(","))
if a>=c or b>=d:
    print("请重新输入并保证a<c,b<d")
    exit()
image=cv2.imread(r"D:\bizhi\puregreen.png")
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)[b:d,a:c]
h,s,v=cv2.split(hsv_image)
h,s,v=np.mean(h),np.mean(s),np.mean(v)
def color(h,s,v):
    if v<=46:
        return "黑"
    elif s<=43 and  46<v<=220:
        return "灰"
    elif s<=30 and v>=221:
        return "白"
    elif h<=10 or h>156 and s>=43 and v>=46:
        return "红"
    elif 11<=h<25 and s>=43 and v>=46:
        return "橙"
    elif 16<=h<34 and s>=43 and v>=46:
        return "黄"
    elif 35<=h<77 and s>=43 and v>=46:
        return "绿"
    elif 78<=h<99 and s>=43 and v>=46:
        return "青"
    elif 100<=h<124 and s>=43 and v>=46:
        return "蓝"
    elif 125<=h<155 and s>=43 and v>=46:
        return "紫"
color_image=color(h,s,v)
print(f"选中部分的颜色是{color_image}")
