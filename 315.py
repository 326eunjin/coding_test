import itertools
n, m = map(int, input().split())
l = list(map(int, input().split()))
result = 0
comb = list(itertools.combinations(list(set(l)),2))
print(comb)
for i,j in comb:
    result += l.count(i) * l.count(j)
    print(l.count(i), l.count(j))
print(result)
#nC2