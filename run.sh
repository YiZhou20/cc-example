#!/usr/bin/env bash

# Run script for running the two desired features on tweets

# Scripts run with input directory tweet_input and output files to directory tweet_output
python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt