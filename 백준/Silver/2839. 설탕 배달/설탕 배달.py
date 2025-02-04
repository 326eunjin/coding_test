n = int(input())

i = n // 5

while True:
    tmp = n - i * 5
    if tmp % 3 == 0:
        j = tmp // 3
        break
    elif i == 0:
        j = -1
        break
    i -= 1

print(i + j)
