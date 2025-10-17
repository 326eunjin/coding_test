def solution(answers):
    result = {1 : 0, 2:0,3:0}
    r_list=[]
    p1_pattern = [1,2,3,4,5]
    p2_pattern = [2,1,2,3,2,4,2,5]
    p3_pattern = [3,3,1,1,2,2,4,4,5,5]

    p_1 = p1_pattern * (len(answers)//len(p1_pattern)) + p1_pattern[:len(answers)%len(p1_pattern)]
    p_2 = p2_pattern * (len(answers)//len(p2_pattern)) + p2_pattern[:len(answers)%len(p2_pattern)]
    p_3 = p3_pattern * (len(answers)//len(p3_pattern)) + p3_pattern[:len(answers)%len(p3_pattern)]
    for i in range(len(answers)):
        if p_1[i] == answers[i]:
            result[1] +=1
        if p_2[i] == answers[i]:
            result[2] +=1
        if p_3[i] == answers[i]:
            result[3] +=1
    max_value = max(list(result.values()))
    
    for key,value in result.items():
        if value == max_value:
            r_list.append(key)
    r_list.sort()
    return r_list