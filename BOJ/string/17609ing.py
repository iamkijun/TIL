#시간초과

import sys
sys.stdin = open('input.txt','r')

import copy

T = int(input())

for t in range(1,T+1):
    S = list(input())

    ans = 2

    if S == S[::-1]:
        ans = 0
        print(ans)
        continue

    elif S[0] == S[-1] or S[0] == S[-2] or S[1] == S[-1]:
        for i in range(len(S)):
            S_for = copy.deepcopy(S)
            S_for.pop(i)
            if S_for == S_for[::-1]:
                ans = 1
                break
    else:
        ans = 2

    
    print(ans)