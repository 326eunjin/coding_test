n,m = map(list,input().split())
result = 0
if len(n) == len(m):
    i = 0
    while (i < len(n) and n[i] == m[i]):
        i+=1
    tmp = n[:i]
    result += tmp.count('8')
    if (int(''.join(m)) - int(''.join(n)) < 10 and i < len(n)-1 and m[i] == '8'):
        result+=1
print(result)