from itertools import permutations
import math 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def make_nums(combs):
    results = [int(''.join(map(str, p))) for p in combs]
    results = [r for r in results if is_prime(r)]
    return results

def solution(numbers):
    n_list = []
    result = set()
    for i in range(len(numbers)):
        n_list.append(numbers[i])
    for i in range(1,len(numbers)+1):
        combs = permutations(n_list,i)
        tmp_list = make_nums(combs)
        for tmp in tmp_list:
            if tmp not in result:
                result.add(tmp)

    return len(result)