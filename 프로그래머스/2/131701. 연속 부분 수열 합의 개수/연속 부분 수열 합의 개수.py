def solution(elements):
    elements.extend(elements)
    result = set()
    o_len = int(len(elements)/2)
    for i in range(o_len):
        for j in range(o_len):
            subarray_sum = sum(elements[j:j+i+1])
            result.add(subarray_sum)
    return len(result)
