n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# 시작 볼륨 집합
possible = {s}

for i in range(n):
    next_set = set()
    for vol in possible:
        if vol + v[i] <= m:
            next_set.add(vol + v[i])
        if vol - v[i] >= 0:
            next_set.add(vol - v[i])
    possible = next_set

if not possible:  # 아무 볼륨도 못 만들면
    print(-1)
else:
    print(max(possible))  # 가능한 볼륨 중 최댓값
