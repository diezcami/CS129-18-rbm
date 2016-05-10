from collections import defaultdict

dd = defaultdict(int)
dd[1] = 1
dd[2] = 2
dd[3] = 3
dd[4] = 4

for i in dd.items():
    print i