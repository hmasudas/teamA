# 必要モジュールをインポートする
import sqlite3

# データベースに接続する
conn = sqlite3.connect('example.db' , isolation_level=None)
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE IF NOT EXISTS TABLE member(user_id real, user_name varchar(16), mail_address varchar(100) ,password vachar(256),prefectures_id char(2))''')

# データの挿入
c.execute("INSERT INTO member VALUES (1, 'testです', 'tesuto@co.jp','1234','01')")

# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()