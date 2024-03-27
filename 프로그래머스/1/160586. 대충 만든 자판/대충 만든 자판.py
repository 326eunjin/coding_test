def get_min(keymap, key):
    min = 1000
    for k in keymap:
        try:
            k.index(key)
        except ValueError:
            continue
        if k.index(key) < min:
            min = k.index(key) + 1
    if min == 1000:
        min = -1
    return min
            
def solution(keymap, targets):
    answer = []
    for i in targets:
        tmp = 0
        for j in range(0,len(i)):
            if get_min(keymap,i[j]) == -1:
                tmp = -1
                break
            else:
                tmp += get_min(keymap,i[j])
        answer.append(tmp) 
    return answer