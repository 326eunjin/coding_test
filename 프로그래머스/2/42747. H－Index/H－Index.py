result = []
def get_h_index(num,citations):
    tmp = [i for i, value in enumerate(citations) if value >= num]
    if len(tmp) >= num and len(citations) - len(tmp) <= num:
        result.append(num)
        return
    return

def solution(citations):
    citations = sorted(citations,reverse=True)
    for i in range(len(citations),0,-1):
        get_h_index(i,citations)
    if len(result) == 0:
        return 0
    else:
        return result[0]
