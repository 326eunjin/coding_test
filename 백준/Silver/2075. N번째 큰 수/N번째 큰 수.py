import heapq

h = []
n = int(input())
for _ in range(n):
    for i in map(int, input().split(" ")):
        if len(h) < n:
            heapq.heappush(h, i)
        else:
            if i > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, i)
            else:
                pass
print(sorted(h, reverse=True)[-1])
