def solution(a, b):
    answer = 0
    mi = min(a,b)
    ma = max(a,b)
    for i in range(mi,ma+1):
        answer+=i
    return answer