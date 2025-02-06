l = []
answer = [[0 for _ in range(5)] for _ in range(5)]
call = []
for _ in range(5):
    l.append(list(map(int, input().split(" "))))

for _ in range(5):
    call.extend(list(map(int, input().split(" "))))


def make_answer_checked(i):
    for y in range(5):
        for x in range(5):
            if l[y][x] == i:
                answer[y][x] = 1
                return y, x


def check_if_bingo(y, x):
    result = 0
    if all(answer[i][i] for i in range(5)):
        result += 1

    if all(answer[i][4 - i] for i in range(5)):
        result += 1

    for row in range(5):
        if all(answer[row][i] for i in range(5)):
            result += 1

    for col in range(5):
        if all(answer[i][col] for i in range(5)):
            result += 1

    if result >= 3:
        return True
    else:
        return False


total = 0
for i in range(len(call)):
    y, x = make_answer_checked(call[i])
    if check_if_bingo(y, x):
        total = i
        break

print(total + 1)
