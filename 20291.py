n = int(input())
l = []
res = {}
for _ in range(n):
    l.append(input().split('.'))

for i in l:
    if i[1] not in res:
        res[i[1]] = 1
    else:
        res[i[1]] +=1
for i ,j in dict(sorted(res.items())).items():
    print(i+' '+str(j))