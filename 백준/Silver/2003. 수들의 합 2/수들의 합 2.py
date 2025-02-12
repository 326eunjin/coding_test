n, m = map(int, input().split(" "))

l = list(map(int, input().split(" ")))

i = 0
j = 0
cnt = 0
tmp = 0
while i <= len(l) and j <= len(l):
    if sum(l[i:j]) >= m:
        i += 1
    else:
        j += 1
    if sum(l[i:j]) == m:
        cnt += 1
        tmp = 0

print(cnt)
