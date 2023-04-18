input = input()
x = ord(input[0])-96
y = int(input[1])
cnt = 0

# a b 대소 비교 가능?
# print('a' < 'b') 안됨
if (x+1 <= 8 and y-2 >= 1):
    cnt += 1
if (x+2 <= 8 and y-1 >= 1):
    cnt += 1
if (x+2 <= 8 and y+1 <= 8):
    cnt += 1
if (x+1 <= 8 and y+2 <= 8):
    cnt += 1
if (x-1 >= 1 and y+2 <= 8):
    cnt += 1
if (x-2 >= 1 and y+1 <= 8):
    cnt += 1
if (x-2 >= 1 and y-1 >= 1):
    cnt += 1
if (x-1 >= 1 and y-2 >= 1):
    cnt += 1

print(cnt)
