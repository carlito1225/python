#使用者輸入: input('提示內容")會得到字串
import math #載入數學工具資源

r=input("請輸入半徑:")
r=float(r)
print(r,type(r))

area= math.pow(r,2) * math.pi # 亦可作 area=r**2 * math.pi

print("面積:",area)
