n = int(input())
l = list(map(int, input().split()))
result = 0
for i in l:
    if l.count(i)>=i:
        result+=1
        for _ in range(i):
            l.remove(i)

print(result)