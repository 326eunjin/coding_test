def next_permutation(s):
    # 문자열을 리스트로 변환
    s = list(s)
    n = len(s)

    # 1. 뒤에서부터 첫 번째 감소하는 부분을 찾는다.
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i == -1:
        return None  # 더 이상 순열이 없으면 None을 리턴

    # 2. 그 부분보다 큰 숫자 중 가장 작은 숫자를 찾아서 교환
    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    # 3. 교환
    s[i], s[j] = s[j], s[i]

    # 4. 뒤의 부분을 오름차순으로 정렬
    s[i + 1:] = sorted(s[i + 1:])
    
    return ''.join(s)

i = int(input())
l = [input() for _ in range(i)]

result = []

for s in l:
    flag = False
    for i in range(-2, -len(s) - 1, -1):
        tmp = s[i:]
        next_per = next_permutation(tmp)
        if next_per and next_per != tmp:
            result.append(s[: len(s) - len(tmp)] + next_per)
            flag = True
            break
    if not flag:
        result.append(s)

for i in result:
    print(i)
