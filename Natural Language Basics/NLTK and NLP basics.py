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



# Example per


