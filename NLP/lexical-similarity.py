import nltk
from fuzzywuzzy import process


file = open('bible_turkish.txt', encoding='utf-8')
raw = file.read()
tokens = nltk.word_tokenize(raw)

fileFreq = nltk.FreqDist(tokens)
i = 0
high = []
low = []

for k, v in fileFreq.items():
    if len(k) > 1:
        if 5 < v and i < 100:
            i += 1
            print(k, v)
            high.append(k)

        if 5 >= v and i < 100:
            i += 1
            low.append(k)

print("\n \n \n \n")
print("Low Frequency        High Frequency     ")
for word in low:
    value = process.extract(word, high)
    similarWord = value[0][0]
    similarity = value[0][1]
    print(word, "    ----->    ", similarWord,  "\n")
