import sys
sys.stdin = open("input.txt","r")

T = 10

for t in range(1,T+1):
    N, S = map(str, input().split())

    s= str(S)

    stk = []

    for val in s:
        stk.append(val)
        try:
            if stk[-1] == stk[-2]:
                stk.pop(-1)
                stk.pop(-1)
        except:
            pass

    print(f'#{t}', ''.join(stk))