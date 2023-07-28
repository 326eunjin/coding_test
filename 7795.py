# times = int(input())
# ret = []
# for _ in range(times):
#     cnt=0
#     n,m = map(int, input().split())
#     a=list(map(int,input().split()))
#     a.sort(reverse=True)
#     b=list(map(int,input().split()))
#     b.sort(reverse=True)
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i]>b[j]:
#                 cnt+=1
#     ret.append(cnt)

# for i in range(len(ret)):
#     print(ret[i])

times = int(input())
ret = []
for _ in range(times):
    cnt = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    i, j = 0, 0
    while i < n and j < m:
        if a[i] > b[j]:
            cnt += m - j
            i += 1
        else:
            j += 1

    ret.append(cnt)

for i in range(len(ret)):
    print(ret[i])
