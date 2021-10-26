# SQLAlchemy はデータベース(DB)を object のように扱えるライブラリである。
# 今回は DB との連結を担当する。
# models.py の User クラスで、どのような object として扱うかを決める。
from flask import Flask,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import User

app = Flask(__name__)

# test.db (DB) と連結するための object である engine を作り、DB を session に代入する。
engine = create_engine('sqlite:///test.db')
session = sessionmaker(bind=engine)()

# /index2 へアクセスがあった場合に、 index2.html を返す。
@app.route("/index2")

# index2 関数を定義する。
# sessionn の全データを、User クラスで定義された object に代入し、users として返す。
# この users を html 内の users に代入する。

def index2():
    users = session.query(User).all()
    return render_template('index2.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)