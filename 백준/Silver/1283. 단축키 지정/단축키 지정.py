cnt = int(input())

word_list = [list(input().split()) for _ in range(cnt)]
abv = []
result = []

for words in word_list:
    flag = False
    if len(words) == 1:
        if words[0][0].upper() not in abv:
            result.append(["[" + words[0][0] + "]" + words[0][1:]])
            abv.append(words[0][0].upper())
            flag = True
        else:
            for index in range(len(words[0])):
                if words[0][index].upper() not in abv:
                    result.append(
                        [
                            words[0][:index]
                            + "["
                            + words[0][index]
                            + "]"
                            + words[0][index + 1 :]
                        ]
                    )
                    abv.append(words[0][index].upper())
                    flag = True
                    break
    else:
        tmp = []
        for word_index in range(len(words)):  # 문장 내 단어 순서
            if words[word_index][0].upper() not in abv:
                abv.append(words[word_index][0].upper())
                tmp.extend(words[:word_index])
                tmp.append("[" + words[word_index][0] + "]" + words[word_index][1:])
                tmp.extend(words[word_index + 1 :])
                result.append(tmp)
                flag = True
                break
        if flag == False:
            for word_index in range(len(words)):
                for i in range(1, len(words[word_index])):
                    if words[word_index][i].upper() not in abv:
                        abv.append(words[word_index][i].upper())
                        tmp.extend(words[:word_index])
                        tmp.append(
                            words[word_index][:i]
                            + "["
                            + words[word_index][i]
                            + "]"
                            + words[word_index][i + 1 :]
                        )
                        tmp.extend(words[word_index + 1 :])
                        result.append(tmp)
                        flag = True
                        break
                if flag == True:
                    break
    if flag == False:
        result.append(words)

for i in result:
    print(" ".join(i))
