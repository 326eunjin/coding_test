input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1),
         (1, 2), (-1, 2), (-2, 1)]  # 튜플로 이루어진 리스트
# 튜플이 뭐냐면 즉 리스트의 요솟값은 변화가 가능하고 튜플의 요솟값은 변화가 불가능하다 리스트랑 비슷한데 달라
cnt = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if (next_row >= 1 and next_row <= 8 and next_column <= 8 and next_column >= 1):
        cnt += 1

print(cnt)
