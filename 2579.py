n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
if n == 1:
    print(array[0])
elif n == 2:
    print(max(array[0], array[1]))
else:
    d = [0] * 300
    d[0] = array[0]
    d[1] = array[1] + array[0]
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    print(d[n - 1] + d[0])
