
n, k, m = input().split()
n = int(n)
k = int(k)
m = int(m)
num = []
num = input().split()
# for i in range(len(input().split)):
#     num.append(input().split())
for i in range(len(num)):
    num[i] = int(num[i])
num.sort(reverse=True)
ret = 0
i = 0
j = 0
while (j < k):
    for _ in range(m):
        ret += num[0]
    ret += num[1]
    j += (m+1)
print(ret)
