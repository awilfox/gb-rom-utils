#!/usr/bin/env python3

from collections import defaultdict

d = defaultdict(int)

with open('sortedlist', 'r') as f:
    for line in f:
        d[line.split('\t', maxsplit=1)[0]] += 1

for k,v in d.items():
    print('{v}\t{k} ROMs'.format(v=v, k=k))

