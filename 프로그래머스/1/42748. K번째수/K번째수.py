def solution(array, commands):
    answer = []
    for i in commands:
        tmp = sorted(array[i[0]-1:i[1]])
        if len(tmp) != 1:
            answer.append(tmp[i[2]-1])
        else:
            answer.append(tmp[0])
    return answer