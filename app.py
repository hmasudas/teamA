from oseti import oseti
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from struct import *
import sqlalchemy.engine
from sqlalchemy import event
@event.listens_for(sqlalchemy.engine.Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()

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
class Member(db.Model):
    __tablename__ = 'member'

    user_id = db.Column(Integer, primary_key=True)
    user_name = db.Column(VARCHAR(16),nullable=False)
    mail_address = db.Column(VARCHAR(100),nullable=False)
    password = db.Column(VARCHAR(256),nullable=False)
    prefectures_id = db.Column(VARCHAR(2),nullable=False)

class Image(db.Model):
    __tablename__ = 'image'

    image_id = db.Column(Integer, primary_key=True)
    image_binary = db.Column(VARCHAR(50),nullable=False)

class post(db.model):
    __tablename__ = 'post'

    post_id = db.Column(Integer, primary_key=True)
    user_id = db.Column(INTEGER,db.ForeignKey('member.user_id'),nullable=False)
    post_text = db.Column(VARCHAR(256),nullable=False)
    image_id = db.Column(Integer,db.foreignkey('image.image_id'))
    post_date = db.Column(DATE,nullable=False)

class taglist(db.model):
    __tablename__ = 'taglist'

    tag_id = db.Column(INTEGER,primary_key=True)
    tag_name = db.Column(VARCHAR,nullable=False)

class tagmanage(db.model):
    __tablename__ = 'tagmanage'

    tag_manage_id = db.Column(INTEGER,primary_key=True)
    tag_name = db.Column(INTEGER,db.Foreignkey('taglist.tag_id'),nullable=False)
    post_id = db.Column(INTEGER,db.Foreignkey('post.post_id'),nullable=False)

# DBの作成
db.create_all()
    

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/DBINFO', methods=['POST', 'GET'])
def bokinbox():
    if request.method == 'POST':
        yourname = request.form['yourname']
        age = request.form['age']
        flask = Member(YOURNAME=yourname, AGE=age)#,my_blob=pack('H', 365)
        db.session.add(flask)
        db.session.commit()
        db.session.close()
        Member_infos = db.session.query(
            Member.ID, Member.YOURNAME, Member.AGE).all() #,Member.my_blob
        return render_template('db_info.html', Member_infos=Member_infos)

# 127.0.0.1/DBINFO:5000に遷移したときの処理
@app.route('/search', methods=['GET'])
def search():
        user = db.session.query(Member.YOURNAME).filter(Member.AGE == 20).all()

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