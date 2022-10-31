from itertools import combinations
import math

def solution(nums):
    cnt = 0
    for a in combinations(nums,3):
        candidate = sum(a)

        for i in range(2,int(candidate**0.5+1)):
            if candidate % i == 0:
                break
        else:        
            cnt+=1

    return cnt