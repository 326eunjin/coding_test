n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True  # 시작 볼륨

for i in range(1, n + 1):
    for vol in range(m + 1):
        if dp[i - 1][vol]:  # 이전에 vol 가능했다면
            if vol + v[i - 1] <= m:
                dp[i][vol + v[i - 1]] = True
            if vol - v[i - 1] >= 0:
                dp[i][vol - v[i - 1]] = True

ans = -1
for vol in range(m, -1, -1):  # 큰 볼륨부터 확인
    if dp[n][vol]:
        ans = vol
        break

print(ans)
