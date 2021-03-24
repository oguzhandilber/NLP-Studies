import spacy
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_lg')
df = pd.read_csv('DrinkReviews.csv')
df.head()
df.shape
df.drop(columns=['Unnamed: 0','Bottle_name'],inplace=True)
df.head()
sentence_vector = [nlp(x).vector for x in df[df['Brand']=='Yamazaki']['Review_Content'].values]
sentence_vector = np.stack( sentence_vector, axis=0 )
sentence_vector.shape
svd = TruncatedSVD(n_components=10)
svd_sentences = svd.fit_transform(sentence_vector)
svd_sentences
cos_sim=cosine_similarity(svd_sentences,svd_sentences)
pd.DataFrame(cos_sim)[7].sort_values(ascending=False)[:10]
kelime = input()
my_sentece_vec = np.stack([nlp(kelime).vector])
sentence_vector = np.append(sentence_vector,my_sentece_vec,axis=0)
sentence_vector.shape
svd_sentences = svd.fit_transform(sentence_vector)
cos_sim=cosine_similarity(svd_sentences,svd_sentences)
print(pd.DataFrame(cos_sim)[457].sort_values(ascending=False)[:10])
sayi = int(input())
print(df[df['Brand']=='Yamazaki']['Review_Content'][sayi])