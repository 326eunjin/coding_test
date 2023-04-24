arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):  # i에서 0까지 -1씩 줄여나감
        if (arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)
