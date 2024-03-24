from collections import Counter
from itertools import combinations
from sys import stdin
n,m = map(int,input().split())
l = []
res = 0
for i in range(n):
    line = stdin.readline().strip()
    l.append(list(int(j) for j in str(line)))

for i in range(n-1):
    tmp = Counter(l[i])
    result = [key for key, value in tmp.items() if value >= 2]
    for t in result:
        rest_list = list(filter(lambda e:l[i][e] == t, range(len(l[i]))))
        perm = list(combinations(rest_list, 2))
        for j in perm:
            length = (j[1]-j[0])
            if(i+length <= n-1  and j[0] <= m-1 and j[1] <= m-1 and l[i+length][j[0]] == t and l[i+length][j[1]] == t):
                if pow(length+1,2) >= res:
                    res = pow(length+1,2)
if (n == 1 or m == 1 or res == 0):
    print(1)
else:
    print(res)