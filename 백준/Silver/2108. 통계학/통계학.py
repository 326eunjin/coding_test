import sys
from collections import Counter
n=int(sys.stdin.readline())
l=[]
tmp1 = 0
tmp3 = []
tmp4 = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()

for i in range(len(l)):
    tmp1 +=l[i]
tmp3 = Counter(l).most_common()
print(round(tmp1/len(l)))
print(l[int((len(l)-1)/2)])
common = tmp3[0][1]
for a,b in tmp3:
    if b == common:
        tmp4.append(a)
if (len(tmp4) > 1):
    print(tmp4[1])
else:
    print(tmp4[0])
print(max(l)-min(l))
