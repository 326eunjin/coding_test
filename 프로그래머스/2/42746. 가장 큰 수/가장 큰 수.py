def solution(numbers):
    tmp = []
    answer=''
    for i in numbers:
        tmp.append(str(i))
    tmp.sort(key=lambda x: x*3, reverse=True)
    if tmp[0] == '0':
        return "0"
    for j in tmp:
        answer+=j
    return answer