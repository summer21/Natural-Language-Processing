# NLTK  collection of python modules for natural language processing.

# tokenization
# machine Learning
# resources
# chunking
# bigram
# ngram
# frequency distribtions
# normalization
# tagging
# trigram

# Importing Libraries

import nltk
from nltk.corpus import inaugural
import pandas as pd
import matplotlib.pyplot as plt


# Text Count

# For practising i will loading the gutenberg project books
for book in nltk.corpus.gutenberg.fileids():
    print(book)

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
print(md[:8])
print(md.count('whale'))
print(md.count('boat'))
print(md.count("laptop"))
print(len(md))

md_set = set(md)
print(len(md_set))

# no of time each word in book

print(len(md)/len(md_set))

# store books as sentences

md_sents = nltk.corpus.gutenberg.sents("melville-moby_dick.txt")
print(len(md_sents))
print(len(md)/len(md_sents))



# Example words per sentance trends

print(inaugural.fileids())

for speech in inaugural.fileids():
    total_word = len(inaugural.words(speech))
    print(str(total_word) + " Title: " + speech)

# if you find that output as list. I generally used list comprehension

speech_len = [ (len(inaugural.words()), speech) for speech in inaugural.fileids()]
print(speech_len)
print(max(speech_len))
print(min(speech_len))

# Find out the average no of words per sentence

for speech in inaugural.fileids():
    words_total = len(inaugural.words(speech))
    sents_total = len(inaugural.sents(speech))
    avg_word_per_sents = words_total/sents_total
    print(avg_word_per_sents, speech)

# Best way to show this information as plot or visualize .
# Making the data frame using the python

data = pd.DataFrame([int(speech[:4]), len(inaugural.words(speech)) / len( inaugural.sents(speech))] for speech in inaugural.fileids())
data.columns = ["Year","Average WPS"]
print(data.head(10))

plt.interactive(False)
data.plot("Year", figsize= (15,5))
plt.show()


