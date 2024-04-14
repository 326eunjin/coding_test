def solution(n):
    answer = n+1
    while True:
        n_bin = list(bin(n))
        if list(bin(answer)).count('1') == n_bin.count('1'):
            break
        answer+=1
    return answer