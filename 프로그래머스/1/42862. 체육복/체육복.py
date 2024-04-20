def solution(n, lost, reserve):
    answer = 0
    cnt = 0
    lost = sorted(lost)
    reserve = sorted(reserve)
    reserve_tmp = []
    for j in reserve:
        if j in lost:
            lost.remove(j)
        else:
            reserve_tmp.append(j)
    for i in reserve_tmp:
        if (i-1) in lost:
            lost.remove(i-1)
        elif (i+1) in lost:
            lost.remove(i+1)
            cnt += 1
    answer = n - len(lost)
    return answer