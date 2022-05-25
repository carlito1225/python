# sep= 區隔符號 (預設是空白 ' ')
# end= 結尾符號 (預設是斷行符號 \n)
symbol='2330.TW'
name='台積電'
price=550
print(symbol,end=";")
print(name,end=";")
print(price)
print(symbol, name, price, sep=";")