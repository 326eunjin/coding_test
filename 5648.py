#reversed_str = "".join(reversed(string))
l = []

while True:
        # 입력으로부터 한 줄을 받아서 int로 변환하여 리스트에 추가
        # extend(): 리스트에 원소를 추가할 때, 원소를 개별적으로 풀어서(분리해서) 리스트의 원소로 추가
        l.extend(map(str , input().split()))
        
        # 입력된 원소의 개수가 첫 번째 원소와 같으면 입력 종료
        if len(l) == int(l[0])+1:
            break
del l[0]
for i in range(len(l)):
    l[i]=int("".join(reversed(l[i])))

l.sort()
for i in range(len(l)):
    print(l[i])