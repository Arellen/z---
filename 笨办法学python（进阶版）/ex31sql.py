import sqlite3

# 连接到数据库
conn = sqlite3.connect('Sample_db.db')

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询语句
data = cursor.execute('SELECT * FROM person')

# 读取查询结果
rows = cursor.fetchall()
for row in rows:
    print(row)

# # 更新数据
cursor.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (6, "baby", "leo1n", 44, 0, "18765453321", 2300, 322))

# # 插入数据
# cursor.execute('INSERT INTO mytable VALUES (?, ?)', (3, 'Alice'))

# # 更新数据
# cursor.execute('UPDATE mytable SET name = ? WHERE id = ?', ('Bob', 1))

# # 删除数据
# cursor.execute('DELETE FROM mytable WHERE id = ?', (2,))

# # 提交事务并关闭连接
conn.commit()
conn.close()