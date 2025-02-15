n = int(input())
m = int(input())
cnt = 0

hand = [1, 2, 3, 4, 5, 4, 3, 2]
# indices = [i for i, x in enumerate(hand) if x == n]

if n == 5:
    result = 8 * m + 4
elif n == 1:
    result = 8 * m
else:
    a = m // 2
    b = m % 2
    result = a * 8
    if b != 0:
        if n == 2:
            result += 7
        elif n == 3:
            result += 6
        elif n == 4:
            result += 5
    else:
        if n == 2:
            result += 1
        elif n == 3:
            result += 2
        elif n == 4:
            result += 3

print(result)
