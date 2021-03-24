from nltk.wsd import lesk
import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

# -----------------------------------------------------------------------------------

# Remove Stop Words . Word Stemming . Return new tokenised list.


def filteredSentence(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()  # lemmatizes the words
    ps = PorterStemmer()  # stemmer stems the root of the word.

    stop_words = set(stopwords.words("turkish"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)
    return filtered_sent

# --------------------------------------------------------------------------------------

# Add synonyms to match list


def synonymsCreator(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

# ---------------------------------------------------------------------------------------

# Cehck and return similarity


def simlilarityCheck(word1, word2):

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0

# -----------------------------------------------------------------------------------------


def simpleFilter(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))
            # for i in synonymsCreator(w):
            # 	filtered_sent.append(i)
    return filtered_sent


if __name__ == '__main__':

    zamanfile = codecs.open("zaman.txt", 'r', "utf-8")
    sent2 = zamanfile.read().lower()
    uydufile = codecs.open("uydu.txt", 'r', 'utf-8')
    sent1 = uydufile.read().lower()
    sent3 = "start"


    while(sent3 != "end"):

        sent3 = input("Enter Query: ").lower()

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_sent3 = []

        counter1 = 0
        counter2 = 0
        sent31_similarity = 0
        sent32_similarity = 0

        filtered_sent1 = simpleFilter(sent1)
        filtered_sent2 = simpleFilter(sent2)
        filtered_sent3 = simpleFilter(sent3)

        for i in filtered_sent3:

            for j in filtered_sent1:
                counter1 = counter1 + 1
                sent31_similarity = sent31_similarity + simlilarityCheck(i, j)

            for j in filtered_sent2:
                counter2 = counter2 + 1
                sent32_similarity = sent32_similarity + simlilarityCheck(i, j)

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_sent3 = []

        filtered_sent1 = filteredSentence(sent1)
        filtered_sent2 = filteredSentence(sent2)
        filtered_sent3 = filteredSentence(sent3)

        sent1_count = 0
        sent2_count = 0

        for i in filtered_sent3:

            for j in filtered_sent1:

                if(i == j):
                    sent1_count = sent1_count + 1

            for j in filtered_sent2:
                if(i == j):
                    sent2_count = sent2_count + 1

        if((sent1_count + sent31_similarity) > (sent2_count+sent32_similarity)):
            print ("Dünyanın uydusu")
        else:
            print( "Zaman birimi")


    print ("\nTERMINATED")                     