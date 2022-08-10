import time
import requests
import pandas as pd
import io
import sqlite3
from datetime import date , timedelta

#抓取每日股價並存入資料庫中
def create_record(date):
    url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1659530272690' % date
    r = requests.get(url)
    lines = r.text.split("\n")
    newlines = []
    for line in lines:
        if len(line.split('",')) == 17:
            newlines.append(line.replace('=', '')) #去除有'='的內容
    #將 newlines 裡面的每一筆資料透過 \n 來串接
    # [1,2,3], [4,5,6] => "1,2,3\n4,5,6"
    data ="\n".join(newlines)
    df = pd.read_csv(io.StringIO(data)) #將字串data轉乘csv檔案格式並給pd來讀取
    # 將全部資料變為str(字串)
    df = df.astype(str)
    # 除去內容中有逗號[,]的資料
    df = df.apply(lambda s: s.str.replace(',', ''))
    #加入日期
    df['交易日'] = date
    # 設定 交易日 與 證券代號 為 index
    df = df.set_index(['交易日','證券代號'])
    # 去除非數字資料 (coerce 表示若轉換失敗就賦予NaN)
    df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
    #將欄位有NaN的都移除
    df = df.dropna(axis=1, how="all")
    #先將 df 存成 csv 再轉存到 sqlite
    df.to_csv("price.csv", encoding="utf-8") # utf-8_sig
    conn = sqlite3.connect('../資料庫/財經資料庫.db')
    df.to_sql('price', conn, if_exists='append')


if __name__ == '__main__':
    begin_day = date(2010, 1, 2)
    today = date.today()
    diff = today - begin_day
    all_date = (begin_day + timedelta(n) for n in range(diff.days + 1))
    for single_date in all_date:
        print(str(single_date), end=" ")
        try:
            time.sleep(7)
            yyyy = single_date.strftime("%Y")
            mm = single_date.strftime("%m")
            dd = single_date.strftime("%d")
            target_date = yyyy + '' + mm + '' + dd
            create_record(target_date)
            print('新增完成: ')
        except Exception as e:
            print('無資料: ' + str(e))
