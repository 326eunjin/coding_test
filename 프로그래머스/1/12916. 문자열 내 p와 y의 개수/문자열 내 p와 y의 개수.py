def solution(s):
    answer = True
    i = s.count('p') + s.count('P')
    j = s.count('y') + s.count('Y')
    print(i)
    if i == 0 and j == 0:
        return True
    elif i == j:
        return True
    else:
        return False