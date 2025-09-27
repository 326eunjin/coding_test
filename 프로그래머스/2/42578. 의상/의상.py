from itertools import combinations

def solution(clothes):
    result = {}
    result_value = 1
    for c in clothes:
        key = c[-1]
        value = c[:-1]
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    keys = list(result.keys())
    for k in keys:
        result_value *= len(result.get(k))+1
    return result_value - 1
