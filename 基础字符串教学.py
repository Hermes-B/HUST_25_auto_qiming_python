# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 22:19:19 2023

@author: never
"""

a='hello'
print(a.rfind('e'))#查找并返回所在位置

b='abcdefFFFF'
print(b.count('F'))

a=a.replace('l','q',2)#一定写a=xxx，不然没用
print(a)

print(b.split('b'))#切分并删除b
print(b.partition('b'))#切分并保留b
print(b.rpartition('b'))#同上

c='hello\nworld'
c=c.splitlines()
print(c)

a=a.capitalize()
print(a)

a=a.upper()
print(a)

a=a.lower()
print(a)

a=a.title()#每个字符串首字母大写
print(a)

e='   abcdefFFFFF g  '
print(e.startswith('a'))

print(a.ljust(15,'x'))
print(a.rjust(15,'x'))
print(a.center(15,'x'))

print(e.lstrip())
print(e.rstrip())
print(e.strip())#去掉两侧空格
print(e.replace(' ',''))#去掉所有空格

