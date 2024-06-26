# from collections import deque
# def solution(phone_book):
#     answer = True
#     phone_book = deque(phone_book)
#     phone_book = sorted(phone_book, key = len)
#     for i in range(len(phone_book)):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[j].find(phone_book[i]) == 0:
#                 return False
#     return answer

def solution(phone_book):
    phone_book.sort()  # 전화번호를 사전순으로 정렬
    
    for i in range(len(phone_book) - 1):
        # 현재 전화번호가 다음 전화번호의 접두어인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True
