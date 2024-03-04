n, m = map(int, input().split())
l = []
result=[]
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)
for i in range(2,n+1):
    result[i]=result[i-1]
