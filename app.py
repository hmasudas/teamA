from oseti import oseti
from flask import Flask, render_template, url_for, request, redirect

# coding: UTF-8

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

@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:

        return render_template('image_test.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)