def get_nearest(num: int):
    i = 0
    while True:
        if ((i) * (i + 1) / 2) <= num and num < ((i + 1) * (i + 2) / 2):
            break
        i += 1
    return i


def get_tri(num: int):
    return num * (num + 1) // 2


def get_tri_tri(num: int):
    for i in range(get_nearest(num), 0, -1):
        t1 = num - get_tri(i)
        if t1 <= 0:
            continue
        for j in range(get_nearest(t1), 0, -1):
            t2 = t1 - get_tri(j)
            if t2 <= 0:
                continue
            for k in range(get_nearest(t2), 0, -1):
                t3 = t2 - get_tri(k)
                if t3 == 0:
                    return 1
    return 0



times = int(input())
result = []
for i in range(times):
    tmp = int(input())
    result.append(get_tri_tri(tmp))
for r in result:
    print(r)
