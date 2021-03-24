from nltk import pos_tag, word_tokenize
from collections import Counter
import nltk

file = open('tedx_turkish.txt',encoding='utf-8')
raw = file.read()


lower_case = raw.lower()
tokens = nltk.word_tokenize(lower_case)

print(tokens)