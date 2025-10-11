#numpy基本功能介绍，后续opencv中会大量用到

import numpy as np
# #创造指定数据类型数组
# list=[1,2,3]
# n1=np.array(list,dtype=float)
# print(n1)
# print(n1.dtype)

# #创造指定维数数组
# nd1=[1,2,3]
# nd2=np.array(nd1,ndmin=3)

# print(nd2)
# #创造未初始化数组
# n=np.empty([2,3])#两行三列的未初始化数组
# print(n)

# #创造全0/1数组
# ls0=np.zeros((3,3),np.uint8)#三行三列，数字类型为uint8的纯0数组
# ls1=np.ones((3,3),np.uint8)#三行三列，数字类型为uint8的纯1数组
# print(ls0,"\n",ls1)

# #创造随机数组
# nr1=np.random.randint(1,10,10)#生成从1到10（左闭右开）的十个整数
# print(nr1)
# nr2=np.random.randint(10,size=20)#生成10以内（不含10）的20个整数
# print(nr2)
# nr3=np.random.randint(1,10,(2,5))#size一栏可填多维
# print(nr3)

# #可以不使用循环进行数组间运算
# nc1=np.array([1,2,3])
# nc2=np.array([3,4,5])

# #数组间的四则运算
# print(nc1+nc2)
# print(nc1-nc2)
# print(nc1*nc2)
# print(nc1/nc2)
# print(nc1**nc2)

# #都为对相同位置的数作对应计算(若无法一一对应会报错)
# #数组间逻辑运算
# print(nc1==nc2)
# print(nc1>nc2)
# print(nc1<nc2)
# print(nc1<=nc2)
# print(nc1>=nc2)
# print(nc1!=nc2)

# #输出形式也都为数组(bool值))
# #数组复制，修改
# na=np.array([1,2])
# nb=na.copy()
# nb[0]=8#修改nb不会影响na
# print(na,nb)

# #切片式索引
# ns1=np.array([0,1,2,3])
# print(ns1[0:2:1])#分别为起始位置，终止位置，步长，左闭右开
# print(ns1[2::])#冒号内不填代表从0开始；一直到末尾；步长为1
# print(ns1[-1::-1])#负数为反向索引，0123对应-4-3-2-1

# #二维数组索引
# nt=np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(nt[0])
# print(nt[1,2])
# print(nt[-1,0])
# print(nt[-1])
# #按(a,b)索引对应坐标，也可反向索引，若仅有一个数则为索引对应行

# #二维数组切片式索引(按一维分别索引行数，列数)
# print(nt[:2,1:])#第二行以前，第一列以后所有数
# print(nt[1:2,::2])
# print(nt[:,:1])#第零列所有数