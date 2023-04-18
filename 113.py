n = int(input())
cnt = 0

# 3 13 23 33 43 53 30 31 32 34 35 36 37 38 39->15
if (n < 3):
    cnt = n+1
elif (n < 13):
    cnt = n
elif (n == 23):
    cnt = n - 2
else:
    cnt = n-1

print((n+1)*60*60-45*45*(cnt))  # 3이 한번이라도 안 나올 확률
