n = int(input())
s = list(map(int, input().split(" ")))

result = []

# 뒤에서부터 첫 번째로 감소하는 부분을 찾음
for i in range(-2, -len(s) - 1, -1):
    if s[i] < s[i + 1]:
        # 그 다음 큰 숫자를 찾아 교환
        for j in range(-1, -len(s) - 1, -1):
            if s[j] > s[i]:
                s[j], s[i] = s[i], s[j]
                result = s[: i + 1] + sorted(s[i + 1 :])
                flag = True
                break
        break

# 만약 순열이 마지막 순열이라면 -1 출력
if len(result) == 0:
    print("-1")
else:
    print(*result)
