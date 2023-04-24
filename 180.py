n = int(input())
arr = [0] * n


def setting(data):
    return (data[1])


for i in range(n):
    arr[i] = list(map(str, input().split()))
    arr[i][1] = int(arr[i][1])

sorted(arr, key=setting, reverse=True)
# sorted(arr, key = lamda student:student[1])
for i in range(n):
    print(arr[i][0], end=' ')
# end = ' '
