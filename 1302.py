n = int(input())
my_list = []
result = {}
for i in range(n):
    my_list.append(input())

for i in range(n):
    result[my_list[i]] = my_list.count(my_list[i])

sorted_by_value = sorted(result.items(), key=lambda x: (-x[1], x[0]))  # 숫자 역순, 문자열 정순 정렬

print(sorted_by_value[0][0])
