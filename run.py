from flask import Flask, render_template, request  # Flaskの操作に必要なモジュールをインポート
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String  # DBのテーブルの型をインポート


# Flaskの立ち上げ

app = Flask(__name__)
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
    
# 127.0.0.1:5000に遷移したときの処理
@app.route('/')
def rroute():
    return render_template('index.html')

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/DBINFO', methods=['POST', 'GET'])
def bokinbox():
    if request.method == 'POST':
        yourname = request.form['yourname']
        age = request.form['age']
        flask = FLASKDB(YOURNAME=yourname, AGE=age)
        db.session.add(flask)
        db.session.commit()
        db.session.close()
        FLASKDB_infos = db.session.query(
            FLASKDB.ID, FLASKDB.YOURNAME, FLASKDB.AGE).all()
        return render_template('db_info.html', FLASKDB_infos=FLASKDB_infos)

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/search', methods=['GET'])
def search():
        user = db.session.query(FLASKDB.YOURNAME).filter(FLASKDB.AGE == 20).all()

        return render_template('search.html', user=user)

@app.route('/index3', methods=['GET'])
def index3():
        return render_template('index3.html')

# python app立ち上げ
if __name__ == '__main__':  
    app.run()
