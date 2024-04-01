def solution(n, words):
    answer = []
    tmp = []
    for i in range(len(words)):
        if i >= 1 and words[i][0] != words[i-1][-1]:
            break
        if words[i] not in tmp:
            tmp.append(words[i])
        else:
            break
    i +=1
    if tmp == words:
        return [0,0]
    if i%n == 0:
        answer.append(i-(int(i/n)-1)*n)
        answer.append(int(i/n))
    else:
        answer.append(i-int(i/n)*n)
        answer.append(int(i/n)+1)
    return answer