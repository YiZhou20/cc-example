# Script that calculates the total number of times each word has been tweeted.
_author_ = 'Yi'

import sys

cmd_args = sys.argv
input_file = cmd_args[1]
output_file = cmd_args[2]

word_count = {}

with open(input_file) as file_tweets:
    for tweet in file_tweets:
        tweet_stripped = tweet.strip() # remove '\n'
        tweet_by_word = tweet_stripped.split(' ')
        for word in tweet_by_word:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

with open(output_file,'w') as feature_one:
    for word in sorted(word_count):
        feature_one.write(word + ' ' + str(word_count[word]) + '\n')