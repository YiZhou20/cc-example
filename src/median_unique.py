# Script that calculates the median number of unique words per tweet.
_author_ = 'Yi'

import bisect
import numpy
import sys

cmd_args = sys.argv
input_file = cmd_args[1]
output_file = cmd_args[2]

median_index = 0
is_odd = 0
tweet_lengths = []

with open(output_file,'w') as feature_two:
    with open(input_file) as file_tweets:

        for tweet in file_tweets:
            if is_odd == 0:
                is_odd = 1
            else:
                is_odd = 0

            tweet_by_word = tweet.split(' ')
            tweet_length = len(tweet_by_word)
            bisect.insort_left(tweet_lengths,tweet_length)

            if is_odd == 1:
                moving_median = tweet_lengths[median_index]
            else:
                moving_median = numpy.median([tweet_lengths[median_index], tweet_lengths[median_index+1]])
                median_index += 1

            feature_two.write('%.1f\n' % moving_median)