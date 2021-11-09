from oseti import oseti
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from struct import *
#スコアの取得
def getScore(list):

  positive = 0
  negative = 0

  #リストないの感情を計算
  for i in list:
    positive += i["positive"]
    negative += i["negative"]

  #スコアの計算
  score = -1
  if positive+negative > 0:
    score = positive/(positive+negative)

  #判定
  result = ""
  if score == -1:
    result = "判定できません"
  elif score < 0.5:
    result = "ネガティブ"
  else:
    result = "ポジティブ"

  return result

def getAnalyzer(txt):
    analyzer = oseti.Analyzer()
    return analyzer.count_polarity(txt)

app = Flask(__name__)

# Flaskの立ち上げ
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
    my_blob = Column(BLOB)
# DBの作成
db.create_all()
    

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/DBINFO', methods=['POST', 'GET'])
def bokinbox():
    if request.method == 'POST':
        yourname = request.form['yourname']
        age = request.form['age']
        flask = FLASKDB(YOURNAME=yourname, AGE=age,my_blob=pack('H', 365))
        db.session.add(flask)
        db.session.commit()
        db.session.close()
        FLASKDB_infos = db.session.query(
            FLASKDB.ID, FLASKDB.YOURNAME, FLASKDB.AGE,FLASKDB.my_blob).all()
        return render_template('db_info.html', FLASKDB_infos=FLASKDB_infos)

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/search', methods=['GET'])
def search():
        user = db.session.query(FLASKDB.YOURNAME).filter(FLASKDB.AGE == 20).all()

        return render_template('search.html', user=user)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():

    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))

    # POSTメソッドの場合
    else:
        # リクエストフォームから「名前」を取得
        txt = request.form['txt']
        name = getScore(getAnalyzer(txt))

        # nameとtitleをindex.htmlに変数展開
        return render_template('index.html',name=name)

@app.route('/login', methods=['GET'])
def login():
        return render_template('login.html')

@app.route('/profile', methods=['GET'])
def profile():
        return render_template('profile1.html')

@app.route('/profile2', methods=['GET'])
def profile2():
        return render_template('profile2.html')

@app.route('/index2', methods=['GET'])
def index2():
        return render_template('index2.html')
@app.route('/ranking', methods=['GET'])
def ranking():
        return render_template('ranking.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)