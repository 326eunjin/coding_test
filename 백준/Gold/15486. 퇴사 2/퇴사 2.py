import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)  # n일까지 최대 이익 저장

for i in range(n - 1, -1, -1):  # 역순 탐색
    if i + t[i] <= n:  # 상담 가능
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
    else:  # 상담 불가능 → 다음 날 이익 이어받음
        dp[i] = dp[i + 1]

print(dp[0])
