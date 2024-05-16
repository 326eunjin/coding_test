# from collections import deque
# def solution(prices):
#     answer = []
#     prices = deque(prices)
#     while prices:
#         tmp = prices.popleft()
#         cnt = 0
#         m = min(prices)
#         if tmp <= m:
#             cnt = len(prices)
#         else:
#             cnt = prices.index(m) + 1
#         answer.append(cnt)
        
#     return answer
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
        
    return answer
