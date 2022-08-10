import requests
import pandas as pd
import io
import sqlite3

date = '20220803'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1659530272690' % date
r = requests.get(url)
#print(r, r.text)
lines = r.text.split("\n")
newlines = []
for line in lines:
    if len(line.split('",')) == 17:
        newlines.append(line.replace('=', ''))
#print(newlines)
data = '\n'.join(newlines)
df = pd.read_csv(io.StringIO(data))
#print(df)
# 將全部資料變為str(字串)
df = df.astype(str)
#除去內容中有逗號[,]的資料
#def func(s):
#    return s.str.replace(',','')
#df = df.apply(func)
df = df.apply(lambda s:s.str.replace(',',''))
# 將證券代號設定為index
df = df.set_index('證券代號')
#去除非數字資料 (coerce 表示若轉換失敗就賦予nan)
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
#將欄位有NaN的都移除
# axis (0:index, 1:column) 預設是0
# how: 'any', 'all' 預設是 'any
#'any' 如果有存在任何NaN, 則刪除該行或該列
#'all' 如果所有內容皆為NaN, 則刪除該行或該列
df = df.dropna(axis=1, how="all")
#print(df)
#查出今日收盤價比開盤價高出 8% 的股票代碼
#print(df[df['收盤價'] / df['開盤價'] >= 1.08])
#將 df 存入到 price.csv
df.to_csv('price.csv', encoding='utf_8_sig')
#將price.csv資料存入資料庫
conn = sqlite3.connect('twse.db')
df.to_sql('price', conn, if_exists='replace') #若日期相同要使用 replace
df.to_sql('price', conn, if_exists='append')  #若日期不相同要用 append
