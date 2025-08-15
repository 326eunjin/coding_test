from itertools import combinations


def get_xp(start: tuple, xp: list):
    sum = 0
    two = combinations(start, 2)
    for t in two:
        sum += xp[t[0]][t[1]] + xp[t[1]][t[0]]
    return sum


result = 10**9
total = int(input())

idx = [i for i in range(total)]
xp = []
for _ in range(total):
    xp.append(list(map(int, input().split(" "))))

comb = combinations(idx, total // 2)

for start in comb:
    if 0 not in start:
        continue
    link = tuple(set(idx) - set(start))
    xp_result = abs(get_xp(start, xp) - get_xp(link, xp))
    if xp_result < result:
        result = xp_result

print(result)
