from itertools import combinations
def solution(numbers):
    answer = set()
    tmp = list(combinations(numbers,2))
    for i in tmp:
        answer.add(sum(i))
    answer = sorted(list(answer))
    return answer