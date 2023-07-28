import collections # collections 모듈 불러오기

len,max = map(int,input().split())
l = list(map(int,input().split()))
frequency=collections.Counter(l)
l=sorted(l,key=lambda x:(-frequency[x],l.index(x)))
#sorted 함수는 기본적으로 안정 정렬(stable sort)을 수행하므로, 빈도수가 같은 요소들의 원래 순서를 유지합니다.
for i in range(len-1):
    print(l[i],end=' ')
print(l[len-1])