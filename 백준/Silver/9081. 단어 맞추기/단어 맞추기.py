n = int(input())
l = list(input() for _ in range(n))

result = []

# 뒤에서부터 첫 번째로 감소하는 부분을 찾음
for s in l:
    flag = False
    s = list(s)
    for i in range(-2, -len(s) - 1, -1):
        if s[i] < s[i + 1]:
            # 그 다음 큰 숫자를 찾아 교환
            for j in range(-1, -len(s) - 1, -1):
                if s[j] > s[i]:
                    s[j], s[i] = s[i], s[j]
                    result.append(s[: i + 1] + sorted(s[i + 1 :]))
                    flag = True
                    break
            break
    if flag == False:
        result.append(s)

for i in result:
    print(''.join(i))
