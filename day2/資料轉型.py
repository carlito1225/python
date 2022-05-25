#資料轉型
#字串轉數字: int(字串變數)
#字串轉浮點數:float(字串轉浮點數)
#數字轉字串: str(數字變數)

chinese = "90" #國文考90分
english = "85" #英文考85分
math = 70 #數學考70分
#請求出平均
print(type(chinese))   #將chinese字串內容轉int
chinese = int(chinese)
print(type(chinese))

print(type(english))
english = int(english)
print(type(english))

sum=(chinese+english+math)
print("總分:"+str(sum))


avg=(int(chinese)+int(english)+math)/3
print('平均:',avg,"分")

print("平均:",+(sum//3),"分")

