n = input()
m = input()
cnt = 0
while True:
    tmp = n.find(m)
    if tmp == -1:
        break
    n = n.replace(m,"*",1)
    cnt +=1

print(cnt)