from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # (index, sum)
    count = 0

    while queue:
        index, total = queue.popleft()

        if index == len(numbers):  # 마지막 숫자까지 처리
            if total == target:
                count += 1
        else:
            num = numbers[index]
            queue.append((index + 1, total + num))  # + 선택
            queue.append((index + 1, total - num))  # - 선택

    return count
