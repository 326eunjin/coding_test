n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)  # a.sort()
b = sorted(b, reverse=True)  # b.sort(reverse=True)

for i in range(k):
    if (a[i] < b[i]):
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
