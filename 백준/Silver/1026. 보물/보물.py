def get_min(b_dict,num):
    val_list=[]
    for i in b_dict:
        if list(i.keys())[0] == num:
            val_list.append(list(i.values())[0])
    result = min(val_list)
    b_dict.remove({num:result})
    return a_tmp[result]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_dict=[]
tmp = sorted(b)
a_tmp = sorted(a,reverse=True)
answer = 0
for i in range(len(tmp)):
    b_dict.append({tmp[i]:i})
for i in range(len(b)):
    tt = get_min(b_dict,b[i])
    answer += b[i] * tt

print(answer)
