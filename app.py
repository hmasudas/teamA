from oseti import oseti
from flask import Flask, render_template, url_for, request, redirect

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

@app.route('/profile', methods=['GET'])
def profile():
        # nameとtitleをindex.htmlに変数展開
        return render_template('profile.html',title='プロフィール')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)