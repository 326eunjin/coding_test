n = int(input())
dp = [0 for _ in range(n + 1)]  # 횟수 저장


def get_tri(num: int):
    if num == 1:
        dp[num] = 1
    else:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]


get_tri(n)
print(dp[n] % 10007)
