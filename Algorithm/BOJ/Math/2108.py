import sys
sys.stdin = open('Math/input.txt','r')

N = int(input())

li = []

for _ in range(N):
    num = input()

    li.append(int(num))

import math

#1. 산술평균
if N == 1:
    print(li[0])
else:
    print(round(sum(li)/N))

#2. 중앙값
li.sort()
if N >=3:
    print(li[len(li)//2])
else:
    print(li[0])

#3. 최빈값
from collections import Counter

nums = Counter(li)
if N == 1:
    print(nums.most_common(1)[0][0])
else:
    if nums.most_common(2)[0][1] == nums.most_common(2)[1][1]:
        print(nums.most_common(2)[1][0])
    else:
        print(nums.most_common(2)[0][0])



#4. 범위
if N == 1:
    print(0)
else:
    print(max(li)-min(li))