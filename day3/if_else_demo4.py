# if...else 精簡用法
#欲求出 X 是奇數還是偶數
import random as r
x= r.randint(1,10)
print("x:",x)
#判斷 x 是奇數還是偶數
if x %2 ==0:
    print("偶數")
else:
    print("奇數")

#if ... else 精簡用法
result = "偶數" if x %2 ==0 else "奇數"
print(result)
