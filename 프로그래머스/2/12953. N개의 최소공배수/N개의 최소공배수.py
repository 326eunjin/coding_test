import math
def solution(arr):
    arr = sorted(arr)
    result = 1
    for i in range(len(arr)):
        result = int(result * arr[i] / math.gcd(result,arr[i]))
    return result