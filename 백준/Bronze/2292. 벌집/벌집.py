x = int(input())


def get_cnt(x: int):
    if x == 1:
        return 1
    else:
        n = 2
        while True:
            if 3 * (n - 2) * (n - 1) + 1 < x <= 3 * (n - 1) * n + 1:
                return n
            n += 1

print(get_cnt(x))
