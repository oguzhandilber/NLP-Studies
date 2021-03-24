import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec


f = open('tur_wikipedia.txt', "r", encoding = "utf8")
text = f.read()

t_list = text.split("\n")
corpus = []
for cumle in t_list:
    corpus.append(cumle.split())

#print(corpus[:10])
model2 = Word2Vec.load("word2.model")


print(model2.similar_by_word('kadın'))
#print(model2.wv["kadın"])
#your_word_vector = model2.wv["cumartesi"]
#print(model2.most_similar(positive=[your_word_vector], topn=5))


