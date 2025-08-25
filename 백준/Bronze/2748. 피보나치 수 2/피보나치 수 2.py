l = [0 for _ in range(100)]


def pibo(n: int):
    if n < 2:
        l[n] = n
    else:
        if l[n] == 0:
            l[n] = pibo(n - 1) + pibo(n - 2)
    return l[n]


n = int(input())
print(pibo(n))
