n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(list(int, input().split())))
    min = min(data)
    result = max(min, result)

print(result)
