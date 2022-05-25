name, age ="John",18
print(name, age)
print(type(name),type(age))

print(age*2)
print(name*2)
print(name*age)
print(age+age)
print(name+name)
#print(name+age) #執行錯誤
print(name+str(age)) #將age的執行當下轉成string

#浮點數
r=3.14
v=3.14e2 #科學記號(浮點數)
print(r,v)
print(type(r),type(v))

#綜合練習
a,b,c,d=10,20.5,True,"mary"
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))
#如何讓a,b,c,d 4個變數相加 "+"
#print(a+b+c+d) #錯誤
print(str(a+b)+str(c)+str(d))
print(str(a)+str(b)+str(c)+str(d))

#刪除變數
score=100
print("分數:",score)
print("分數:" + str(score))
del score
print(score)
#print(score) 產生NameError:name 'score' is not defined

