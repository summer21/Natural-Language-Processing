# Parse a single tweet
import pandas as pd                         #importing libraries

tweets =pd.read_csv('so_many_tweets.csv')  

first_tweet = tweets['Text'][0]             # first tweet in the dataset
word_in_tweet = first_tweet.split(' ')        # a list of words in the 
for word in word_in_tweet:                  # for each word in the list
	if "$" in word:
		print ("This tweet about: ",word)


