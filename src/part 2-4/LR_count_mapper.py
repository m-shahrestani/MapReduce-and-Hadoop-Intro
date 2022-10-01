#!/usr/bin python3
import sys                                                                                                
import re

pattern = re.compile(r''',(?=(?:(?:[^"]*"){2})*[^"]*$)''')
biden = ('#JoeBiden', '#Biden')
trump = ('#DonaldTrump', '#Trump')
valid_sources = ['Twitter Web App', 'Twitter for iPhone', 'Twitter for Android']

for tweet in sys.stdin:                                                                            
  tweet = tweet.strip()                                                  

  tweet_info = pattern.split(tweet)
  tweet_text = tweet_info[2]
  try:
    tweet_likes = int(float(tweet_info[3]))
    tweet_retweets = int(float(tweet_info[4]))
    tweet_sources = tweet_info[5]
  except ValueError:
    tweet_likes = 0
    tweet_retweets = 0
    tweet_sources = 'null'

  biden_likes = 0
  trump_likes = 0
  both_likes = 0
  biden_retweets = 0
  trump_retweets = 0
  both_retweets = 0
  biden_sources = [0, 0, 0]
  trump_sources = [0, 0, 0]
  both_sources = [0, 0, 0]

  found_trump = any(term in tweet_text for term in trump)
  found_biden = any(term in tweet_text for term in biden)
  
  
  if found_biden and not found_trump:
    biden_likes += tweet_likes
    biden_retweets += tweet_retweets
    if tweet_sources == valid_sources[0]:
    	biden_sources[0] = 1
    if tweet_sources == valid_sources[1]:
    	biden_sources[1] = 1
    if tweet_sources == valid_sources[2]:
    	biden_sources[2] = 1

  if found_trump and not found_biden:
    trump_likes += tweet_likes
    trump_retweets += tweet_retweets
    if tweet_sources == valid_sources[0]:
    	trump_sources[0] = 1
    if tweet_sources == valid_sources[1]:
    	trump_sources[1] = 1
    if tweet_sources == valid_sources[2]:
    	trump_sources[2] = 1
  
  if found_trump and found_biden:
    both_likes += tweet_likes
    both_retweets += tweet_retweets
    if tweet_sources == valid_sources[0]:
    	both_sources[0] = 1
    if tweet_sources == valid_sources[1]:
    	both_sources[1] = 1
    if tweet_sources == valid_sources[2]:
    	both_sources[2] = 1


  print ('%s\t%s\t%s\t%s\t%s\t%s' % ('both', both_likes, both_retweets, both_sources[0], both_sources[1], both_sources[2]))
  print ('%s\t%s\t%s\t%s\t%s\t%s' % ('biden', biden_likes, biden_retweets, biden_sources[0], biden_sources[1], biden_sources[2]))
  print ('%s\t%s\t%s\t%s\t%s\t%s' % ('trump', trump_likes, trump_retweets, trump_sources[0], trump_sources[1], trump_sources[2]))
