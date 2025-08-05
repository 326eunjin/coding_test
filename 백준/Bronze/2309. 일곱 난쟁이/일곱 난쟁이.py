from itertools import combinations

l = [int(input()) for _ in range(9)]
total = sum(l)
comb = list(combinations(l, 2))
for c in comb:
    if total - sum(c) == 100:
        break

l.remove(c[0])
l.remove(c[1])
l.sort()
for i in l:
    print(i)
