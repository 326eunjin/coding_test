l = input()
num = 0
while num <= int(l):
    if int(l) == num + sum(int(digit) for digit in str(num)):
        break
    num += 1
if num >= int(l):
    num = 0

print(num)
