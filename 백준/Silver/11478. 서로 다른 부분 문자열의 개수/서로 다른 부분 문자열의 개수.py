n = input()
s = set()

for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        s.add(n[i:j])

print(len(s))
