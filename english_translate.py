from bs4 import BeautifulSoup

import requests
import pandas as pd

url = 'url'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

contents = soup.find_all('h3', class_='検証した結果のクラス名')

d_list = []
for content in contents:
  d = {
    "word": content.text
  }
  d_list.append(d)
df = pd.DataFrame(d_list)

df.to_csv('csvファイルの名前', index=None, encoding='utf-8-sig')
