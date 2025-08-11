n = int(input())
l = [1, 2, 3]
for _ in range(n):
    i, j = map(int, input().split(" "))
    idx = l.index(i)
    idx_2 = l.index(j)
    l[idx_2] = i
    l[idx] = j

print(l[0])
