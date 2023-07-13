str = input()
l = []
for i in range(len(str)):
    l.append(int(str[i]))
cnt_b = 0
cnt_w = 0
for i in range(len(l)-1):
    if (l[i] == 0):
        while(1):
            if (i != len(l)-1 and l[i+1]==0):
                i+=1
                if (i != len(l)-1 and l[i+1]==1):
                    cnt_w+=1
            else:
                break
    else:
        while(1):
            if (i!= len(l)-1 and l[i+1]==1):
                i+=1
                if (i != len(l)-1 and l[i+1]==0):
                    cnt_b+=1
            else:
                break
if (cnt_w < cnt_b):
    print(cnt_w)
else:
    print(cnt_b)