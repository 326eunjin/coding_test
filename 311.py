n = int(input())
l = list(map(int, input().split())) # 2 3 1 2 2
result = 0
# for i in l: # 2
#     if l.count(i)>=i: # 3 >=2 
#         result+=1 
#         for _ in range(i):
#             l.remove(i) # 2 3 1
l.sort(reverse=True)
for i in range(len(l)):
    if len(l) != 0:
        result+=1
        for _ in range(l[0]):
            del l[0]
print(result)