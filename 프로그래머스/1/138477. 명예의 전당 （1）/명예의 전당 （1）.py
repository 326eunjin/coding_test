def solution(k, score):
    answer = []
    tmp = []
    if k >= len(score):
        for i in range(0,len(score)):
            tmp.append(score[i])
            answer.append(min(tmp))
    else: 
        for i in range(0,k):
            tmp.append(score[i])
            answer.append(min(tmp))
        for i in range(k,len(score)):
            if score[i] >= min(tmp):
                t = min(tmp)
                tmp.remove(t)
                tmp.append(score[i])
            answer.append(min(tmp))
    return answer