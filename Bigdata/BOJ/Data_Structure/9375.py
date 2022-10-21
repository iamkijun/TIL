'''
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
'''

import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())

    dic = {}

    for i in range(N):
        name, type = input().split()
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1

    val_li = []
    for k,v in dic.items():
        val_li.append(v)

    ans = 1
    for val in val_li:
        ans *= (val+1)
    
    ans -=1
    
    print(ans)
