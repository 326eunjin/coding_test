def find_integer_solution(a,b,k):
    big = max(a,b)
    small = min(a,b)
    for y in range(1, k // small + 1):
        x = (k - small * y) / big
        if x.is_integer() and x >= 0:
            print(y)
            print(int(x))
            return

n, k = map(int, input().split())
d = [0] * (n+1)
d[0] = '1x'
d[1] = '1y'
d[2] = '1x+1y'
d[3] = '1x+2y'
for i in range(4,n+1):
    first = d[i-1].split('+')
    second = d[i-2].split('+')
    tmp_1= int(first[0][:-1])+int(second[0][:-1])
    tmp_2= int(first[1][:-1])+int(second[1][:-1])
    d[i]=(str(tmp_1)+'x+'+str(tmp_2)+'y')

exp = d[n-1].split('+')

find_integer_solution(int(exp[0][:-1]),int(exp[1][:-1]),k)
