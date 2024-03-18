from collections import Counter
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = []
d= {}
for _ in range(n):
    tmp = input().strip()
    if len(tmp)>=m:
        l.append(tmp)
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
l = sorted(d,key=lambda x: (-d[x], -len(x),x))
for j in l:
    print(j)