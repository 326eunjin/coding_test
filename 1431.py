import re

n = int(input())
str_arr = []
num = 0
for _ in range(n):
    input_str = input()
    numbers = re.sub(r'[^0-9]', '', input_str)
    num = 0
    for i in range(len(numbers)):
        num += int(numbers[i])
    str_arr.append([input_str, num])

str_arr.sort(key=lambda x: (len(x[0]), x[1],x[0]))
#.sort(key=len)
for i in range(len(str_arr)):
    print(str_arr[i][0])
