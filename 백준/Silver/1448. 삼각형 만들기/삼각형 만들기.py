import sys

n = int(sys.stdin.readline().rstrip())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

l = sorted(l, reverse=True)
result = -1

for i in range(len(l)-2):
    if l[i] < l[i + 1] + l[i + 2] and l[i + 1] < l[i] + l[i + 2] and l[i + 2] < l[i] + l[i + 1]:
        result = l[i] + l[i + 1] + l[i + 2]
        print(result)
        quit()

print(result)