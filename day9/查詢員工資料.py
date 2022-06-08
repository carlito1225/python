import sqlite3

conn = sqlite3.connect("demo.db") #建立資料庫連線
cursor = conn.cursor() #建立 cursor 才可以操作資料庫
sql = "select id, ename, esalary, did from employee"
cursor.execute(sql) #丟給 sqlite 去執行 sql 語句
rows = cursor.fetchall() #得到因sql指令的紀錄列表
# 透過 for-loop 將資料逐筆顯示
print('全部查詢')
for row in rows:
    print(row[0], row[1], row[2], row[3])

print("薪資 >= 100,000")
for row in rows:
    if row[2] >= 100000:
        print(row[0], row[1], row[2], row[3])

print("薪資 <= 50,000")
for row in rows:
    if row[2] >= 50000:
        print(row[0], row[1], row[2], row[3])

conn.close() #資料庫關閉