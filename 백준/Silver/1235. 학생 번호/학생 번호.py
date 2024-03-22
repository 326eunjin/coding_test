n=int(input())
l=[]
for _ in range(n):
    # l.append(str(list(input()).reverse()))
    l.append(input()[::-1])

for j in range(1,len(l[0])+1):
    s = set()
    for i in l:
        if i[0:j] not in s:
            s.add(i[0:j])
    if len(s) == n:
        print(j)
        quit()

