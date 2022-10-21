import sys
sys.stdin = open('input.txt','r')

S = list(input())

stk = []

cnt = 0

for val in S:
    if val == '(':
        if stk and stk[-1] == ')':
            stk.pop(-1)
        stk.append('(')
        
    else:
        if stk[-1] == '(':
            cnt += len(stk)-1
            
        elif stk[-1] == ')':
            cnt += 1
            stk.pop(-1)

        stk.pop(-1)

        stk.append(')')
    print(cnt)