#關於print的格式化參數
#股票代號 2330.TW
#股票名稱 台積電
#目前市價 550.5
#買進價格 530
#買進股數 6000
#手續費 0.001425 (買賣都要算)
#交易稅 0.003 (賣出要算)
#如何計算投資金額與獲利狀態
import math

symbol= "2330.TW"
name = "台積電"
price=550.5
cost=530.5
shares=6000
fee=0.001425
tax=0.003

#請問買入成本=?
buy_cost=shares*cost
fee_cost=buy_cost*fee
buy_cost_total=buy_cost+fee_cost

print(buy_cost_total)
print(math.floor(buy_cost_total))
print(math.ceil(buy_cost_total))

print("股票:%s 買入股數:%d 買入成本:%.1f" % (name, shares, buy_cost_total))
print("股票:%s 買入股數:%s 買入成本:%s" % (name, format(shares, ","), format(buy_cost_total, ",")))

area = 12345.6789
pos=3; #小數點位數
print(format(int(area*10**pos)/10**pos,","))
print(format(int(area*100)/100,",")) #不使用 %.2f 要得到小數點後2位

print(3*1**3)

x+y=83
2x+4y=240
print(x,y)


