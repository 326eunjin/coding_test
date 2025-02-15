from math import floor

k = int(input())

A, B = map(int, input().split(" "))
A_kcal = int(input())
B_kcal = []
for _ in range(k):
    B_kcal.append(int(input()))
B_kcal = sorted(B_kcal, reverse=True)
result = []


def best_pizza(i):
    tmp = B_kcal[:i]
    kcal = A_kcal + sum(tmp)
    return floor(kcal / (A + B * i))


for i in range(0, k + 1, 1):
    result.append(best_pizza(i))
result = sorted(result, reverse=True)

print(result[0])
