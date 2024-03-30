def solution(s):
    answer = (s[0]).upper()
    for i in range(1,len(s)):
        if (s[i-1] == ' ' and (s[i-1].isdigit() == False) and (s[i].islower() == True)):
            answer+=(s[i].upper())
        elif (s[i-1] != ' ' or (s[i-1].isdigit() == True)) and (s[i].isupper() == True):
            answer+=(s[i].lower())
        else:
            answer+=(s[i])
    return answer