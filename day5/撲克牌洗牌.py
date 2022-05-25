poker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#位置      0,  1,  2,  3,  4,  5,  6,  7,  8,   9,  10, 11 ,12
#洗牌前
print(poker)
#洗牌後
num=poker[0]  #將poker[0]的資料給num
poker[0]=poker[1] #將poker[1]的資料給poker[0]
poker[1]=num #將num的資料給poker[1]
print(poker)
#洗牌

