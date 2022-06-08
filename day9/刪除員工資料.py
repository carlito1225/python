import sqlite3

id = int(input("請輸入員工編號:"))

sql='''
    delete from employee where id = %d 
'''

sql = sql.strip() % (id)
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rowcount = cursor.rowcount  # 異動筆數
print('刪除', rowcount, '筆成功')
conn.commit()  # 提交
conn.close()