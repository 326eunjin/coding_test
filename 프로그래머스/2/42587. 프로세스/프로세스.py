from collections import deque

def solution(priorities, location):
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    answer = 0
    
    while queue:
        cur_doc = queue.popleft()
        is_higher_priority = False
        for doc in queue:
            if cur_doc[1] < doc[1]:
                is_higher_priority = True
                break
        if is_higher_priority:
            queue.append(cur_doc)
        else:
            answer += 1
            if cur_doc[0] == location:
                return answer