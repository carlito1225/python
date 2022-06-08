import sqlite3

id = int(input("請輸入員工編號:"))
ename = input("請輸入員工姓名:")
esalary = int(input("請輸入員工薪資:"))
did = int(input("請輸入部門編號(101,201,301):"))
sql = """
    insert into employee(id, ename, esalary, did)
    values(%d, "%s", %d, %d)
"""

sql = sql.strip() % (id, ename, esalary, did)
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rowcount = cursor.rowcount  # 異動筆數
print('新增', rowcount, '筆成功')
conn.commit()  # 提交
conn.close()
