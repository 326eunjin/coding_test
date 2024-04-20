from collections import deque
n = int(input())
rank = deque()
for _ in range(n):
    tmp = int(input())
    rank.append(tmp)

rank = sorted(rank)
cnt = 0
for i in range(len(rank)):
    if (i+1) != rank[i]:
        cnt += abs((i+1)-rank[i])

print(cnt)