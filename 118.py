n, m = map(int, input().split())
y, x, d = map(int, input().split())
arr = [[0 for j in range(n)] for i in range(m)]
# 얇은 복사 피하려면 이렇게 해야함
for i in range(m):
    arr[i] = list(map(int, input().split()))
tmp_x = 0
tmp_y = 0
arr[y][x] = 1
# 이거 까먹음


def change_loc(d):
    if (d == 0):
        d = 3
    else:
        d -= 1
    return (d)


cnt = 1
while (True):
    tmp_x = x
    tmp_y = y
    if (d == 0):
        if (arr[y][x-1] != 1):  # 안 가봤으면
            cnt += 1
            arr[y][x] = 1
            x -= 1
            d = change_loc(d)
        else:
            d = change_loc(d)
    elif (d == 1):
        if (arr[y-1][x] != 1):  # 안 가봤으면
            cnt += 1
            arr[y][x] = 1
            y -= 1
            d = change_loc(d)
        else:
            d = change_loc(d)
    elif (d == 2):
        if (arr[y][x+1] != 1):  # 안 가봤으면
            cnt += 1
            arr[y][x] = 1
            x += 1
            d = change_loc(d)
        else:
            d = change_loc(d)
    elif (d == 3):
        if (arr[y+1][x] != 1):  # 안 가봤으면
            cnt += 1
            arr[y][x] = 1
            y += 1
            d = change_loc(d)
        else:
            d = change_loc(d)
    if ((arr[y][x-1] == 1 and arr[y][x+1] == 1 and arr[y+1][x] == 1 and arr[y-1][x] == 1)):
        arr[y][x] = 1
        x = tmp_x
        y = tmp_y
        if (arr[y][x] == 1):
            break


print(cnt)
