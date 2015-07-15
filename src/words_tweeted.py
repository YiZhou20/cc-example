# Script that calculates the total number of times each word has been tweeted.
_author_ = 'Yi'

from itertools import groupby
from operator import itemgetter
import sys

cmd_args = sys.argv
input_file = cmd_args[1]
output_file = cmd_args[2]

word_counts = []

with open(input_file) as file_tweets:
    for tweet in file_tweets:

        tweet_stripped = tweet.strip() # remove '\n'
        tweet_by_word = tweet_stripped.split(' ')

        for word in tweet_by_word:
            word_counts.append([word,1])

word_counts.sort()

with open(output_file,'w') as feature_one:
    for this_word, word_group in groupby(word_counts, itemgetter(0)):
        word_total_count = sum(word_count for this_word, word_count in word_group)
        feature_one.write(this_word + '\t' + str(word_total_count) + '\n')