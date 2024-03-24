n,m = map(int,input().split())

six = []
solo = []
for i in range(m):
    i,j = map(int,input().split())
    six.append(i)
    solo.append(j)

six = sorted(six)
solo = sorted(solo)
mot = int(n/6)
if n < 6 or solo[0] * 6 <= six[0]:
    result = (solo[0] * n)
    if result > six[0] and n < 6:
        result = six[0]
else:
    result = mot*six[0]+(n - mot * 6) * solo[0]
    if result >= six[0] * (mot + 1):
        result = six[0] * (mot + 1)

print(result)

