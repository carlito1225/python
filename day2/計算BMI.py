#使用者輸入

h = float(input("請輸入身高(cm):"))
w = float(input("請輸入體重(kg):"))

h=h/100 #cm>m

bmi=w/h**2

print("BMI:",bmi)


