# n,k = int(input().split())
n, k = map(int, input().split())

l = list(range(1, n+1))
result = []
tmp = k - 1
while l :
    result.append(l.pop(tmp))
    tmp += k - 1
    while (tmp >= len(l) and l):
        tmp -= len(l)

print("<" + str(result)[1:-1] + ">")