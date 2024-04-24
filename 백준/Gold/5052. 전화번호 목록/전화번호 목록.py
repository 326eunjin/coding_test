n = int(input())
result = []

def func1(tmp_list):
    tmp_list = sorted(tmp_list)
    for i in range(len(tmp_list) - 1):
        if tmp_list[i+1].startswith(tmp_list[i]):
            return "NO"
    return "YES"

for _ in range(n):
    tmp_list = []
    tmp = int(input())
    for _ in range(tmp):
        tmp_list.append(input())
    result.append(func1(tmp_list))

for i in result:
    print(i)
