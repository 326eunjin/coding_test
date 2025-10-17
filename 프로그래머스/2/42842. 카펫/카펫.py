from math import sqrt, floor
def check_if_fits(brown,x,y):
    if x+y == (brown//2 - 2):
        return True
    else:
        return False
    
def solution(brown, yellow):
    tmp = floor(sqrt(yellow))
    for i in range(1,tmp+1):
        if yellow %i == 0:
            x = yellow//i
            y = i
            print(x,y)
            if check_if_fits(brown,x,y):
                return [x+2,y+2]