n,m=map(int,input().split())
tn = set()
tm = set()
for _ in range(n):
    tn.add(input())

for _ in range(m):
    tm.add(input())
result = sorted(list(tn & tm))
print(len(result))
for i in result:
    print(i)