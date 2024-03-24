input_str = input()
l = []
for i in range(len(input_str)):
    l.append(int(input_str[i]))

l = sorted(l,reverse=True)
for a in l:
    print(a,end="")
print() 