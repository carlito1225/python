import random as r
poker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#位置      0,  1,  2,  3,  4,  5,  6,  7,  8,   9,  10, 11 ,12
#洗牌前
print(poker)
#洗牌後
for i in range(10):
    print("i的值=",i)
    lens=len(poker)-1
    p1 = r.randint(0,lens)
    p2 = r.randint(0,lens)
    num=poker[p1]
    poker[p1]=poker[p2]
    poker[p2]=num

#洗牌後
print(poker)
