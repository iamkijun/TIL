import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = list(input().split())


    stk = []
    a,b = 0,0
    try:
        for val in S:
            if val.isdigit():
                stk.append(val)
            elif val == '*':
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(int(a)*int(b))
            elif val == '/':
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(int(a)//int(b))
            elif val == '+':
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(int(a)+int(b))
            elif val == '-':
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(int(a)-int(b))
            elif val == '.':
                print(f'#{t} {stk[0]}')

            else:
                print(f'#{t} error')
                break
        if stk:

    except:
        print(f'#{t} error')




