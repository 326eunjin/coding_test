n, m = map(int, input().split())
card = []
tmp = []
ret = []
for i in range(n):
    card.append(list(input().split(' ')))

for i in range(n):
    for j in range(m):
        card[i][j] = int(card[i][j])

for i in range(n):
    card[i].sort()
    ret.append(card[i][0])

ret.sort(reverse=True)
print(ret[0])
