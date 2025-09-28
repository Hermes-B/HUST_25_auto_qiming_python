# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:38:28 2023

@author: never
"""
import numpy as np
num=[0 for i in range(1,5)]
print(num)
n=np.arange(5)
print(n)
m=np.array([np.arange(1,4),np.arange(4,7),np.arange(7,10),np.arange(10,13),np.arange(13,16)])
#矩阵首尾扩上号（【】），中间行数用逗号隔开
print(m)
print(m[0:])#获取从第0行到最后一行的元素
print(m[1:3])#获取1至2行元素

print(m[0:5:2])#始，末，步长，从头/到尾可省略不写

k=m.reshape(3,5)#行，列
print(k)
print(m.ravel())
print(m.flatten())

print(np.vstack((k,n)))#中间要有额外括号，拼接列增长列的长度，要求列数相等，拼接行为hstack

print(np.hsplit(n,5))#切割行

for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j])
        
        
print(len(m))#行数
print(len(m[0]))#列数






