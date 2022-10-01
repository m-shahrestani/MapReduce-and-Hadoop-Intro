#!/usr/bin python3
import sys                                                                                                
import re

pattern = re.compile(r''',(?=(?:(?:[^"]*"){2})*[^"]*$)''')

biden = ('#JoeBiden', '#Biden')
trump = ('#DonaldTrump', '#Trump')


for tweet in sys.stdin:                                                                            
  tweet = tweet.strip()                                                  

  tweet_info = pattern.split(tweet)
  tweet_text = tweet_info[2]
  
  tweet_lat = None
  tweet_lon = None
  try:
    tweet_lat = float(tweet_info[13])
    tweet_lon = float(tweet_info[14])
    tweet_time = int(tweet_info[0].split(" ")[1].split(":")[0])
  except ValueError:
    pass
    
  no_geo_available = False
  if not tweet_lat or not tweet_lon:
    no_geo_available = True
  else:
    tweet_lat = float(tweet_lat) 
    tweet_lon = float(tweet_lon)

  
  found_biden = any(term in tweet_text for term in biden)
  found_trump = any(term in tweet_text for term in trump)
 
  if no_geo_available:
    pass 
  elif 9 <= tweet_time <= 17:
    if 40.4772 < tweet_lat < 45.0153 and -79.7624 < tweet_lon < -71.7517:
      print ('%s\t%s\t%s\t%s\t%s' % ('new york',
                                     1 if (found_trump and found_biden) else 0,
                                     1 if (found_biden and not found_trump) else 0,
                                     1 if (found_trump and not found_biden) else 0,
                                     1 if (found_trump or found_biden) else 0))

    elif 32.5121 < tweet_lat < 42.0126 and -124.6509 < tweet_lon < -114.1315:
      print ('%s\t%s\t%s\t%s\t%s' % ('california',
                                     1 if (found_trump and found_biden) else 0,
                                     1 if (found_biden and not found_trump) else 0,
                                     1 if (found_trump and not found_biden) else 0,
                                     1 if (found_trump or found_biden) else 0))
    else:
      pass
