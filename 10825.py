# n = int(input())
# l=[]
# for i in range(n):
#     l.append(list(map(str,input().split())))
#     l[i][1]=int(l[i][1])
#     l[i][2]=int(l[i][2])
#     l[i][3]=int(l[i][3])
# # l=sorted(l,key=lambda x:(-x[1],x[2],-x[3],x[0]))
# l.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
# for i in range(len(l)):
#     print(l[i][0])
n = int(input())
l = []

for i in range(n):
    data = input().split()
    l.append([data[0], int(data[1]), int(data[2]), int(data[3])])

l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(len(l)):
    print(l[i][0])
