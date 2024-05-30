def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)-l+1):
        tmp = int(t[i:i+l])
        if tmp <= int(p):
            answer+=1
    return answer