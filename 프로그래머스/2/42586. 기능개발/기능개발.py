import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    tmp = deque()
    
    # 각 작업이 완료되는데 걸리는 날짜를 계산하여 tmp에 추가
    for i in range(len(progresses)):
        tmp.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    # 첫 번째 작업의 완료일을 설정
    current_max = tmp.popleft()
    count = 1
    
    while tmp:
        # 다음 작업의 완료일을 확인
        next_days = tmp.popleft()
        
        if next_days <= current_max:
            # 현재 작업 그룹에 포함
            count += 1
        else:
            # 새로운 작업 그룹 시작
            answer.append(count)
            current_max = next_days
            count = 1
    
    # 마지막 남은 작업 그룹 추가
    answer.append(count)
    
    return answer
