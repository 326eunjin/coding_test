str = input()
tmp_letter = []
tmp_num = []
for i in range(len(str)):
    if (str[i].isdigit()==True):
        tmp_num.append(int(str[i]))
    else:
        tmp_letter.append(str[i])

# print(str(sorted(tmp_letter)))
print(''.join(sorted(tmp_letter)),end='')
print(sum(tmp_num))