import sqlite3

# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

sql = """SELECT * FROM member"""

for t in c.execute(sql):#for文で作成した全テーブルを確認していく
    print(t)

conn.close()
