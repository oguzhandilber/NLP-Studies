import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import tokenize
from operator import itemgetter
import math


stop_words = set(stopwords.words('english'))
file = " Studies have established that the majority of UFO observations are misidentified conventional objects or natural phenomena—most commonly aircraft, balloons including sky lanterns, satellites, and astronomical objects such as meteors, bright stars and planets. A small percentage are hoaxes.[note 1] Fewer than 10% of reported sightings remain unexplained after proper investigation, and therefore can be classified as unidentified in the strictest sense. While proponents of the extraterrestrial hypothesis (ETH) suggest these unexplained reports are of alien spacecraft, the null hypothesis cannot be excluded that these reports are simply other more prosaic phenomena which cannot be identified due to lack of complete information or due to the necessary subjectivity of the reports. Instead of accepting the null hypothesis, UFO enthusiasts tend to engage in special pleading by offering outlandish, untested explanations for the validity of the ETH. These violate Occam's razor. "

total_words = file.split()
total_words_length = len(total_words)
print(total_words_length)

total_sentences = tokenize.sent_tokenize(file)
total_sent_len = len(total_sentences)
print(total_sent_len)



tf_score = {}
for each_word in total_words:
    each_word =each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word]+=1
        else:
            tf_score[each_word]=1


tf_score.update((x,y/int(total_words_length)) for x, y in tf_score.items())
print("Term frequency scores of words : "  )
print(tf_score )

def check_sent(word, sentences):
    final = [all ([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))



idf_score = {}
for each_word in total_words:
    each_word =each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word]=1

idf_score.update((x,math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
print("IDF scores are:")
print(idf_score)

tf_idf_score = {key: tf_score[key]* idf_score.get(key, 0) for key in tf_score.keys()}
print("TF İDF scores are:")
print(tf_idf_score)

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(),key = itemgetter(1),reverse = True )[:n])
    return result
print("Getting the 3 best results : ")
print(get_top_n(tf_idf_score,3))