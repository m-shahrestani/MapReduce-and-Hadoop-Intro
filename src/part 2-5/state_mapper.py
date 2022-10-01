#!/usr/bin python3
import sys                                                                                                
import re

pattern = re.compile(r''',(?=(?:(?:[^"]*"){2})*[^"]*$)''')
valid_state = ['new york', 'texas', 'california', 'florida']

biden = ('#JoeBiden', '#Biden')
trump = ('#DonaldTrump', '#Trump')


for tweet in sys.stdin:                                                                            
  tweet = tweet.strip()
  tweet_info = pattern.split(tweet)
  tweet_text = tweet_info[2]
  tweet_state = tweet_info[18].lower()
  try:
    tweet_time = int(tweet_info[0].split(" ")[1].split(":")[0])
  except:
    pass

  other_states = False
  no_state_available = False

  no_state_available = not tweet_state

  found_state = ''
  for state in valid_state:
    if state in tweet_state:
      found_state = state
    
  other_states = not found_state
  
  found_biden = any(term in tweet_text for term in biden)
  found_trump = any(term in tweet_text for term in trump)
 
  if no_state_available:
    pass
  elif other_states:
    pass
  else:
    if  9 <= tweet_time <= 17:
      print ('%s\t%s\t%s\t%s\t%s' % (found_state,
                                     1 if (found_trump and found_biden) else 0,
                                     1 if (found_biden and not found_trump) else 0,
                                     1 if (found_trump and not found_biden) else 0,
                                     1 if (found_trump or found_biden) else 0))

