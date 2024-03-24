from collections import Counter

n = list(input())
tmp = Counter(n)
middle = []
res = []
for key, value in tmp.items():
    if value % 2 == 0:
        value = value / 2
    else:
        middle.append(key)
        if value == 1:
            value = 0
        else:
            value = (value - 1) / 2
    tmp[key] = int(value)
if len(middle) > 1:
    print("I'm Sorry Hansoo")
else:
    sorted_tmp = dict(sorted(tmp.items(), key=lambda item: (item[0], -item[1])))
    while list(sorted_tmp.values()).count(0) != len(sorted_tmp):
        for key, value in sorted_tmp.items():
            if value != 0:
                for _ in range(value):
                    res.append(key)
                sorted_tmp[key] = 0
    print(''.join(res)+''.join(middle)+''.join(sorted(res,reverse=True)))

    