from math import floor

first = int(input())
stock = input().split(" ")
stock = [int(i) for i in stock]

bnp = []
timing = []
total = first
for i in range(14):
    bnp.append([total // stock[i], total % stock[i]])
    total = total % stock[i]

total = first

cnt_2 = 0

for i in range(3, 14):
    if stock[i - 3] < stock[i - 2] < stock[i - 1] and cnt_2 > 0:
        # 팔기
        total = stock[i] * cnt_2 + total
        cnt_2 = 0
    elif stock[i - 3] > stock[i - 2] > stock[i - 1] and total >= stock[i]:
        # 사기
        amount = total // stock[i]
        cnt_2 += amount
        total = total % stock[i]
cnt = 0
for i in bnp:
    cnt += i[0]

result_bnp = bnp[-1][1] + cnt * stock[-1]
result_timing = total + cnt_2 * stock[-1]

if result_bnp > result_timing:
    print("BNP")
elif result_timing > result_bnp:
    print("TIMING")
else:
    print("SAMESAME")
