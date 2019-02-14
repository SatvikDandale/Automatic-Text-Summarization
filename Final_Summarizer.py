import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
'''
f = open("main_para.txt", "r")
text = f.read()
f.close()
'''
print("Enter the text that you want to summarize:\n")
text = input()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stopWords = set(stopwords.words("english"))
# print(stopWords)
word_freq = {}
word_list = list(())
no_words = 0
freq_word_total = 0
imp_word = list(())
text_2 = ''

for word in word_tokenize(text):
    word = word.lower()
    if word in punctuations:
        continue
    if word in stopWords:
        continue
    else:
        text_2 += word + " "
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

tags = nltk.pos_tag(word_tokenize(text_2))

for t in tags:
    if t[1] == 'NN' or t[1] == 'NNP' or t[1] == 'NNS' or t[1] == 'NNPS' or t[1] == 'RBR' or t[1] == 'RB' or t[1] == 'RBS' or t[1] == 'JJ' or t[1] == 'JJR' or t[1] == 'JJS' or t[1] == 'VB' or t[1] == 'VBG' or t[1] == 'VBD' or t[1] == 'VBN' or t[1] == 'VBP' or t[1] == 'VBZ':
        imp_word.append(t[0])

for word in word_freq:
    no_words += 1
    freq_word_total += word_freq[word]

avg = freq_word_total / no_words

for word in word_freq:
    if word_freq[word] > avg:
        word_list.append(word)

final_score = {}
initial_score = {}
for sentence in sent_tokenize(text):
    final_score[sentence] = 0
    initial_score[sentence] = 0

for sentence in sent_tokenize(text):
    if (len(re.findall('[0-9]', sentence))) >= 1:
        final_score[sentence] += 1
        initial_score[sentence] += 1
    for w in imp_word:
        if w in sentence:
            final_score[sentence] += 1
            initial_score[sentence] += 1
    for w in word_list:
        if w in sentence:
            final_score[sentence] += 1
            initial_score[sentence] += 1

total_words = 0
for word in word_tokenize(text):
    if word in punctuations:
        continue
    else:
        total_words += 1

len_sent = {}
total_sent = 0
for sentence in sent_tokenize(text):
    for word in word_tokenize(sentence):
        if word in punctuations:
            continue
        else:
            if sentence in len_sent:
                len_sent[sentence] += 1
            else:
                len_sent[sentence] = 1
    total_sent += 1

for sentence in sent_tokenize(text):
    final_score[sentence] = initial_score[sentence] + len_sent[sentence]

avg_len_sent = total_words / total_sent
final_score_total_freq = 0
for sentence in sent_tokenize(text):
    final_score_total_freq += final_score[sentence]

avg_final_score = final_score_total_freq / total_sent
extraction = ''
for sentence in final_score:
    if final_score[sentence] > avg_final_score:
        extraction += ' ' + str(sentence)

print(extraction)
f = open("summary.txt", "w")
f.write(str(extraction))
f.write("\n")
f.close()
