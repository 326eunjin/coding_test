n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))


def b_search(arr, target):
    start = 0
    end = len(arr)-1

    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] == target):
            print("YES", end=' ')
            return
        elif (arr[mid] <= target):
            start = mid + 1
        else:
            end = mid - 1

    print("NO", end=' ')
    return


arr_1 = sorted(arr_1)
for i in arr_2:
    b_search(arr_1, i)
