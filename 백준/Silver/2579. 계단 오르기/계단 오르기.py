n = int(input())
visited = [False for _ in range(n)]
stair = []
dp = [0 for _ in range(n + 1)]
for _ in range(n):
    stair.append(int(input()))
stair.insert(0, 0)


def get_stair(num: int):
    # if visited[i-2] == True and visited[i-1] == False:
    #     tmp1 = dp[i-2] + stair[i]
    # elif visited[i-3] == True and visited[i-2] == False and visited[i-1] == True:
    #     tmp2 = dp[i-1] + stair[i]
    # if tmp1 > tmp2:
    #     dp[i] = tmp1
    #     visited[i] = True
    # else:
    #     dp[i] = tmp2
    #     visited[i] = True
    if num == 1:
        dp[num] = stair[num]
    elif num == 2:
        dp[num] = stair[num] + stair[num - 1]
    elif num == 3:
        dp[num] = stair[num] + max(stair[1], stair[2])
    else:
        dp[1] = stair[1]
        dp[2] = stair[1] + stair[2]
        dp[3] = stair[3] + max(stair[1], stair[2])
        for i in range(4, num + 1):
            dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i]


get_stair(n)
print(dp[n])
