def solution(name, yearning, photo):
    m = {}
    for i in range(len(name)):
        m[name[i]] = yearning[i]
    answer = []
    for tmp in photo:
        res = 0
        for j in tmp:
            if j in m:
                res += m[j]
        answer.append(res)
    return answer