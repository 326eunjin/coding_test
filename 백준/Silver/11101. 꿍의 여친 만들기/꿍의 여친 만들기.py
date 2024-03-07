n = int(input())
first=[]
second=[]
dict_list=[]
slash_list=[]
for _ in range(n):
    first.append(input())
    second.append(input())

for i in range(n):
    comma = first[i].split(',')
    tmp_list = {}
    for comma_item in comma:
        key, value = comma_item.split(':')
        tmp_list[key]= value
    dict_list.append(tmp_list)
    slash = second[i].split('|')
    tmp_list = []
    for k in range(len(slash)):
        tmp_list.append(slash[k].split('&'))
    slash_list.append(tmp_list)
i=k=j=0

max_list=[]
for k in range(0, n):
    max_list=[]
    for i in range(0, len(slash_list[k])):
        max = 0
        for j in range(0, len(slash_list[k][i])):
            if max <= int(dict_list[k][slash_list[k][i][j]]):
                max = int(dict_list[k][slash_list[k][i][j]])
        max_list.append(max)
        j = 0  # j를 초기화하여 다음 내부 반복문을 위해 준비합니다.
    max_list=sorted(max_list)
    print(max_list[0])

