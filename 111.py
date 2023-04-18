n = map(int, input())
# inst = list(map(str, input().split()))
inst = input().split()
curr = [1, 1]

for i in range(len(inst)):
    if (inst[i] == "R" and curr[1] != n):
        curr[1] += 1
    elif (inst[i] == "U" and curr[0] != 1):
        curr[0] -= 1
    elif (inst[i] == "L" and curr[1] != 1):
        curr[1] -= 1
    elif (inst[i] == "D" and curr[0] != n):
        curr[0] += 1
print(curr[0], curr[1])
