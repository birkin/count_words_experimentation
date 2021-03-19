"""
Goal...
- modified version of <https://benhoyt.com/writings/count-words/>
- words sorted by count, and then alphabetically
"""

import collections, pprint

## get word: count --------------------

counts_by_word = {}

with open( './kjvbible.txt', 'r' ) as f:
    for line in f.readlines():
        words = line.split()
        for word in words:
            lwrcase = word.lower()
            if lwrcase in counts_by_word.keys():
                counts_by_word[lwrcase] += 1
            else:
                counts_by_word[lwrcase] = 1
# print( f'counts_by_word, ``{counts_by_word}``' )

## get count: [ 'a', 'b' ] ------------

counts_by_count = {}
for ( key_word, val_count ) in counts_by_word.items():
    # print( f'key_word, ``{key_word}``; val_count, ``{val_count}``' )
    if val_count in counts_by_count.keys():
        counts_by_count[val_count].append( key_word )
        # print( f'counts_by_count[val_count] initially, ``{counts_by_count[val_count]}``' )
        counts_by_count[val_count].sort()
        # print( f'counts_by_count[val_count] after sort, ``{counts_by_count[val_count]}``' )
    else:
        counts_by_count[val_count] = [ key_word ]
# print( f'counts_by_count, ``{counts_by_count}``' )

## sort the counts_by_count dict ------

od = collections.OrderedDict( sorted(counts_by_count.items(), reverse=True) )

for ( key_count, val_words ) in od.items():
    for word in val_words:
        print( f'{word}: {key_count}' )
