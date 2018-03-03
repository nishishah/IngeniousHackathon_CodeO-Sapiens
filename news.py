import html2text
import requests
import nltk
import yaml
import sys
import os
import re
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk import word_tokenize


url = 'https://www.indiatoday.in/top-stories'
res = requests.get(url, timeout=5.0)
html = res.text
# extract the text from the html version
text = html2text.html2text(html)
print(text)
stop_words = set(stopwords.words('english'))
token = word_tokenize(text)
filtered_sentence = [w for w in token if not w in stop_words]

filtered_sentence1 = []

for w in token:
    if w not in stop_words:
        filtered_sentence1.append(w)

print(token)
print(filtered_sentence1)
