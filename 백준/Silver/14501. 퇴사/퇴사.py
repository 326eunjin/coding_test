n = int(input())
l = []
for _ in range(n):
    t, p = map(int, input().split())
    l.append((t, p))

dp = [0] * (n + 1)  # dp[i] = i일부터 얻을 수 있는 최대 수익

for i in range(n - 1, -1, -1):  # 뒤에서 앞으로
    t, p = l[i]
    if i + t <= n:  # 상담이 퇴사 전에 끝나는 경우
        dp[i] = max(p + dp[i + t], dp[i + 1])
    else:           # 상담 못 하는 경우
        dp[i] = dp[i + 1]

print(dp[0])
