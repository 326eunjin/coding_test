def solution(sizes):
    answer = 0
    x = []
    y=[]
    for size in sizes:
        x.append(min(size))
        y.append(max(size))
    
    answer = max(x) * max(y)
    return answer