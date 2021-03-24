from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('trmodel', binary=True)

#print(model.most_similar(positive=["kral","kadın"],negative=["erkek"]))

f = open('tur_wikipedia.txt', "r", encoding = "utf8")
text = f.read()

#two sample sentences
s1 = text
s2 = 'bakmadan seyret'

#calculate distance between two sentences using WMD algorithm
#distance = model.wmdistance(s1, s2)
#distance = model.wv.n_similarity(s1.lower().split(), s2.lower().split())

#print ('distance = %.3f' % distance)



#ms=model.similar_by_word('altın')
#print(ms)

  #word frequency
#for w in model.vocab:
 #    print (w, model.vocab[w].count)

your_word_vector = model.wv["cuma"]
print(model.most_similar(positive=[your_word_vector], topn=5))


