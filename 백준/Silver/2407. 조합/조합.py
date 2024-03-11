n,m = map(int,input().split())
tmp1 = 1
tmp2 = 1
if n == 1:
    print("1")
elif n == m or m == 0:
    print("1")
else:
    if m > (n / 2):
        m = n - m

    for i in range(n,n-m,-1):
        tmp1 *= i
    for j in range(1,m+1):
        tmp2 *= j

    print(int(tmp1 // tmp2))