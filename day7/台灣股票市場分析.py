# 本益比,殖利率,股價淨值比
#  <10 , >5% , <1 (買) >1(賣)
import requests

url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20220525&selectType=ALL"
data = requests.get(url).text

#資料整理
#將有 - 的變成 -1
data = data.replace('"-"','-1')

#將資料中的 " 拿掉
data = data.replace('"','')

#針對每一行 \r 或 \n 將資料切割出來
list=data.split("\r\n")

#['證券代號', '證券名稱', '殖利率(%)', '股利年度', '本益比', '股價淨值比', '財報年/季', '']
pe=10 #本益比 [4]
rate=7 #殖利率 [2]
pb=1 #股價淨值比 [5]
print(list[0])
print(list[1])
print("-------------------------------------------------------------------")

for row in list:
    #print(len(row.split(",")),row)
    val = row.split(",")
    if len(val) == 8 and val[0] !="證券代號":
        #float(字串):字串轉浮點數
        if 0 < float(val[4]) <pe and \
                rate < float(val[2]) and\
                float(val[5]) < pb:
            print(val)


