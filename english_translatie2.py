import csv
import pandas as pd

from googletrans import Translator

translator = Translator()
# with open (r'C:\Users\hachimi\python\scraping_practice\english_translation.csv', encoding='utf-8') as f:
#   reader = csv.reader(f)
#   dict_from_csv = [eng for eng in reader]

data = pd.read_csv('作ったcsvファイルの名前')
japanese_list = []
# print(translator.translate(data[0]))
for i in data['word']:
  dst = translator.translate(i, src = "en", dest = "ja")
  japanese_list.append(dst.text)

data['japanese']=japanese_list
data.to_csv('result.csv',index=None, encoding='utf-8-sig')