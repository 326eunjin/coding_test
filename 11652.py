# from collections import Counter
import sys
n = int(sys.stdin.readline())
# l=[]
# for _ in range(n):
#     l.append(int(sys.stdin.readline()))
# frequency = Counter(l)
# l.sort(key=lambda x :(-frequency[x],x))

# print(l[0])
dic={}
for _ in range(n):
    num = int(sys.stdin.readline())
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
    # l.append(int(sys.stdin.readline()))
dic = sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(dic[0][0])

# 대량의 데이터를 반복적으로 입력받아야 할 때, input()대신 sys.stdin.readline()을 이용하면 성능(속도)이 향상됩니다. 주로 백준 알고리즘 문제를 풀 때 유용합니다.자바에서 Scanner보다 BufferedReader가 빠른것과 같은 맥락입니다.