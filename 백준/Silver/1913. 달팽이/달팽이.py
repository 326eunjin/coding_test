n = int(input())
m = int(input())
l = [[0 for _ in range(n)] for _ in range(n)]

x = 0
y = 0
tmp = n * n

odd = []
for i in range(n, 0, -2):
    odd.append(i)

for i in odd:
    loc = odd.index(i)
    z = (n - 1) - loc
    x = loc
    y = loc
    while True:
        if x == loc and y == loc:
            for _ in range(i - 1):
                l[y][x] = tmp
                if tmp == m:
                    result = [y + 1, x + 1]
                y += 1
                tmp -= 1
            if i == 1:
                l[y][x] = tmp
                if tmp == m:
                    result = [y + 1, x + 1]
                break
        elif x == loc and y == z:
            for _ in range(i - 1):
                l[y][x] = tmp
                if tmp == m:
                    result = [y + 1, x + 1]
                x += 1
                tmp -= 1
        elif x == z and y == z:
            for _ in range(i - 1):
                l[y][x] = tmp
                if tmp == m:
                    result = [y + 1, x + 1]
                y -= 1
                tmp -= 1
        elif x == z and y == loc:
            for _ in range(i - 1):
                l[y][x] = tmp
                if tmp == m:
                    result = [y + 1, x + 1]
                x -= 1
                tmp -= 1
        if tmp == (i - 2) * (i - 2):
            break

for i in range(n):
    for j in range(n - 1):
        print(str(l[i][j]), end=" ")
    print(l[i][-1])

print(str(result[0]) + " " + str(result[1]))
