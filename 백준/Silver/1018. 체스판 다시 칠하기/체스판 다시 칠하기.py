c_board = []
c_board.append([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]] * 4)
c_board.append([[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]] * 4)


def get_min_change(l: list):
    result = []
    for c in c_board:
        cnt = 0
        for i in range(8):
            for j in range(8):
                if l[i][j] != c[i][j]:
                    cnt += 1
        result.append(cnt)
    return min(result)


n, m = map(int, input().split())

origin_l = []
for _ in range(n):
    origin_l.append(list(input()))

for i in range(n):
    for j in range(m):
        if origin_l[i][j] == "W":
            origin_l[i][j] = 0
        else:
            origin_l[i][j] = 1
result = n * m

for r_start in range(n - 7):
    for c_start in range(m - 7):
        sub_matrix = []
        for row in origin_l[r_start : r_start + 8]:
            sub_matrix.append(row[c_start : c_start + 8])
        tmp_result = get_min_change(sub_matrix)
        if tmp_result <= result:
            result = tmp_result
print(result)
