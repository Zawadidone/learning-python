from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(1)

print(d)
