# Script that calculates the median number of unique words per tweet.
_author_ = 'Yi'

import numpy
import sys

cmd_args = sys.argv
input_file = cmd_args[1]
output_file = cmd_args[2]

with open(output_file,'w') as feature_two:
    with open(input_file) as file_tweets:
        tweet_count = 0
        tweet_lengths = []
        for tweet in file_tweets:
            tweet_count += 1
            tweet_by_word = tweet.split(' ')
            tweet_length = len(tweet_by_word)
            tweet_lengths.append(tweet_length)
            moving_median = numpy.median(tweet_lengths)
            feature_two.write(str(moving_median) + '\n')