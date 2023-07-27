from itertools import combinations
n = int(input())
l = list(map(int, input().split()))
ret = 0
sum_map = set()

for i in range(n):
    res = list(combinations(l,i))
    for j in res:
        sum_map.add(sum(j))
while(True):
    if (ret in sum_map):
        ret+=1
    else:
        break
print(ret)