from math import gcd
n,m = map(int,input().split(':'))
g = gcd(n,m)
print(str(n//g)+':'+str(m//g))