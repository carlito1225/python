import sqlite3

id = int(input("請輸入員工編號:"))
esalary = int(input("請輸入員工修改後的薪資:"))
sql='''
    update employee set esalary = %d where id = %d 
'''

sql = sql.strip() % (esalary, id)
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rowcount = cursor.rowcount  # 異動筆數
print('新增', rowcount, '筆成功')
conn.commit()  # 提交
conn.close()