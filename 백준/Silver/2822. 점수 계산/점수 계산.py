d = {}
for i in range(1,9):
    d[i]=int(input())
d = sorted(d.items(),key=lambda item:item[1],reverse=True)
result = 0
l = []

for i in range(0,5):
    result += d[i][1]
    l.append(d[i][0])

print(result)
l = sorted(l)
for i in range(4):
    print(l[i],end=" ")
print(l[4])