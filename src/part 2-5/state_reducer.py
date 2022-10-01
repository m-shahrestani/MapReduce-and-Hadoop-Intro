#!/usr/bin python3
from operator import itemgetter 
import sys

# keep a map of the sum of upvotes of each reddit
state_map = {}

for line in sys.stdin:
    line = line.strip()
    state, both_percent, biden_percent, trump_percent ,count = line.split('\t')

    try:
        both_percent = float(both_percent)
        biden_percent = float(biden_percent)
        trump_percent = float(trump_percent)
        count = int(count)

        both_p = 0
        biden_p = 0
        trump_p = 0
        c = 0
        if state in state_map:
            both_p, biden_p, trump_p, c = state_map[state]

        total = c + count
        if total == 0:
            continue
        new_both_percent = (both_p * c + both_percent * count) / total 
        new_biden_percent = (biden_p * c + biden_percent * count) / total 
        new_trump_percent = (trump_p * c + trump_percent * count) / total 

        state_map[state] = (new_both_percent, new_biden_percent, new_trump_percent, total) 
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the reddits alphabetically;
alphabetic_state_map = sorted(state_map.items(), key=itemgetter(0))

# output to STDOUT
for state, tup in alphabetic_state_map:
    print ('%s\t%s\t%s\t%s\t%s'% (state, tup[0], tup[1], tup[2], tup[3]))
