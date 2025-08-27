n = int(input())
dp = [0 for _ in range(n + 1)]  # 횟수 저장
# l = [0 for _ in range(n+1)] #여기는 숫자 결과 연산고 나서 결과
# l[1] = n


def get_one(num: int):
    if num == 2 or num == 3:
        dp[num] = 1
    else:
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + 1
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)

get_one(n)
print(dp[n])
