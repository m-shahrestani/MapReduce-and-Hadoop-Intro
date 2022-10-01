#!/usr/bin python3
from operator import itemgetter 
import sys

# keep a map of the sum of upvotes of each reddit
like_retweet_map = {}

for line in sys.stdin:
    line = line.strip()
    person, likes, retweets, web, iphone, android = line.split('\t')
    try:
        likes = int(likes)
        retweets = int(retweets)
        web = int(web)
        iphone = int(iphone)
        android = int(android)
        l, r, w, i, a = 0, 0, 0, 0, 0
        if person in like_retweet_map:
            l, r, w, i, a = like_retweet_map[person]

        like_retweet_map[person] = (l + likes, r + retweets, w + web, i + iphone, a + android) 
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the reddits alphabetically;
alphabetic_like_retweet_map = sorted(like_retweet_map.items(), key=itemgetter(0))

# output to STDOUT
for person, tup in alphabetic_like_retweet_map:
    print ('%s\t%s\t%s\t%s\t%s\t%s'% (person, tup[0], tup[1], tup[2], tup[3], tup[4]))
