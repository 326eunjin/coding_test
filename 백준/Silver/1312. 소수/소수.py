A, B, N = map(int, input().split())

# A를 B로 나눈 나머지 계산
A = A % B

# 소수점 N번째 자리 계산
for i in range(N):
    A *= 10
    result = A // B
    A = A % B

print(result)
