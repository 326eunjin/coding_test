import math
n = int(input())
l=[]
tmp = []
cnt = 0
def gcd_of_list(lst):
    if not lst:
        return None
    result = lst[0]
    for i in range(1, len(lst)):
        result = math.gcd(result, lst[i])
    return result

for i in range(n):
    l.append(int(input()))
for i in range(len(l)-1):
    tmp.append(l[i+1]-l[i])
gcd = gcd_of_list(tmp)
for i in range(len(tmp)):
    cnt+=(tmp[i]/gcd)-1
print(int(cnt))