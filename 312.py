str = input()
l = []
for i in range(len(str)):
    l.append(int(str[i]))
result = 0
for i in range(len(l)-1):
    if (l[i]!=0):
        if (i == 0):
            result = l[i] * l[i+1]
        else:
            result *= l[i+1]
    else:
        if (i == 0):
            result = l[i] + l[i+1]
        else:
            result += l[i+1]

print(result)

#1일 때 더해줘야함 단순히 0일때만 아님
