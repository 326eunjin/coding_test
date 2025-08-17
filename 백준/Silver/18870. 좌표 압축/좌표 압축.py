n = int(input())
l = list(map(int, input().split()))

# 정렬 + 중복 제거
tmp = sorted(set(l))

# 값 → 압축 좌표 매핑 (딕셔너리)
mapping = {value: idx for idx, value in enumerate(tmp)}

# 결과 변환
result = [mapping[num] for num in l]

# 출력
print(" ".join(map(str, result)))
