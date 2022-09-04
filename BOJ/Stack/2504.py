import sys
sys.stdin = open('Stack/input.txt','r')

S = list(input())

stk = []
li =[]

ans = 0

a = 1

for i in range(len(S)):
    
    if S[i] == '(':
        a *= 2
        stk.append('(')

    elif S[i] == '[':
        a *= 3
        stk.append('[')
    
    elif S[i] == ')':
        if not stk or stk[-1] == '[':
            ans = 0
            break

        elif S[i-1] == '(':
            ans += a
        
        a = a//2
        stk.pop()

    elif S[i] == ']':
        if not stk or stk[-1] == '(':
            ans = 0
            break

        elif S[i-1] == '[':
            ans += a

        a = a//3
        stk.pop()

if stk:
    print(0)
else:
    print(ans)