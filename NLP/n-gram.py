from nltk import *
from collections import Counter

ngram_counts = Counter()

print("\n")
ngram_count = Counter()
with open('bible english.txt', encoding='utf-8') as bigtxt:
    for l in bigtxt:
        ngram_count.update(Counter(ngrams(l.split(), 3)))

print(ngram_count.most_common(100))