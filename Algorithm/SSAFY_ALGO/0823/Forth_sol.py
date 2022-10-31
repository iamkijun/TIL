import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = list(input().split())


    stk = []

    for ch in S:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            if ch == '.':
                ans = stk.pop()
            else:
                try:
                    b = stk.pop()
                    a = stk.pop()
                    if ch == '+':
                        stk.append(a+b)
                    elif ch == '-':
                        stk.append(a - b)
                    elif ch == '*':
                        stk.append(a * b)
                    elif ch == '/':
                        stk.append(a // b)
                    else:
                        ans = 'error'
                        break
                except:
                    ans = 'error'
                    break

    if stk:
        ans = 'error'

    print(f'#{t} {ans}')