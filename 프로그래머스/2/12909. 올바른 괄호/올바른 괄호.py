from collections import deque
def solution(s):
    answer = True
    tmp = deque()
    for i in s:
        if i ==')' and '(' not in tmp:
            return False
        elif i == ')':
            tmp.remove('(')
        else :
            tmp.append('(')
    if len(tmp) != 0:
        return False
    return True