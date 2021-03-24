import nltk
import matplotlib



file = open('tedx_turkish.txt',encoding='utf-8')
data = file.read()



data = data.split(' ')
fdist1 = nltk.FreqDist(data)
print (fdist1.most_common(50))
fdist1.plot(25,cumulative=False)





