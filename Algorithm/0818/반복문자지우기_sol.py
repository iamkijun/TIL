import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1,T+1):

    S = list(input())

    stk =['',]

    for val in S:
        if val == stk[-1]:
            stk.pop(-1)
        else:
            stk.append(val)

    print(f'#{t} {len(stk)-1}')
