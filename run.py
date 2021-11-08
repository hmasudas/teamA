from flask import Flask, render_template, request  # Flaskの操作に必要なモジュールをインポート
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String  # DBのテーブルの型をインポート
import app

app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.sqlite'  # DBへのパス

# SQLAlchemyでデータベース定義

db = SQLAlchemy(app)

# SQLiteのDBテーブル情報
class FLASKDB(db.Model):
    __tablename__ = 'flask_table'

    ID = db.Column(Integer, primary_key=True)
    YOURNAME = db.Column(String(32))
    AGE = db.Column(Integer)

# DBの作成
db.create_all()

# python app立ち上げ
if __name__ == '__main__':  
    app.run()
