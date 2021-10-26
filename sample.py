from oseti import oseti

def getAnalyzer():
    analyzer = oseti.Analyzer()
    return analyzer.count_polarity('私はとっても幸せ。でも、最悪')

def getScore(list):

  positive = 0
  negative = 0

  #リストないの感情を計算
  for i in list:
    positive += i["positive"]
    negative += i["negative"]

  print(positive)
  print(negative)
  #スコアの計算
  score = positive/(positive+negative)

  return score

print(getScore(getAnalyzer()))