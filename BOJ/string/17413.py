import sys
sys.stdin = open('String/input.txt','r')

s= list(input())

stk = []

ans = ''

for val in s:
    if val == '<':
        if stk:
            ans += ''.join(stk[::-1])
            stk = []
        ans += '<'

    elif val == '>':
        if stk:
            ans += ''.join(stk)+'>'
            stk = []

    elif val == ' ':
        if ans and ans[-1]=='<':
            stk.append(' ')
        elif stk:
            ans += ''.join(stk[::-1])+' '
            stk = []
    else:
        stk.append(val)

if stk:
    ans += ''.join(stk[::-1])

print(ans)
