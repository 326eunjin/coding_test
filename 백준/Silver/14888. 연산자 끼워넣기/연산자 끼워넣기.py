from itertools import permutations

ops = []
cnt = int(input())
num = list(map(int, input().split(" ")))
ops_num = list(map(int, input().split(" ")))
result_list = []

for i in range(len(ops_num)):
    if i == 0:
        ops.extend(["+"] * ops_num[i])
    elif i == 1:
        ops.extend(["-"] * ops_num[i])
    elif i == 2:
        ops.extend(["*"] * ops_num[i])
    elif i == 3:
        ops.extend(["//"] * ops_num[i])

per = set(permutations(ops, cnt - 1))
for p in per:
    if p[0] == "//" and num[0] < 0 and num[1] > 0:
        result = -1 * eval(str(-num[0]) + p[0] + str(num[1]))
    else:
        result = eval(str(num[0]) + p[0] + str(num[1]))
    for i in range(1, cnt - 1):
        if p[i] == "//" and result < 0 and num[i + 1] > 0:
            result = -1 * eval(str(-result) + p[i] + str(num[i + 1]))
        else:
            result = eval(str(result) + p[i] + str(num[i + 1]))
    result_list.append(result)

result_list.sort(reverse=True)
print(result_list[0])
print(result_list[-1])
