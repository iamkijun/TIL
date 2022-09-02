import sys
sys.stdin = open('input.txt','r')

s= list(input())

stk = []

cnt = 0
a = 0
b = 0

for i in range(len(s)):

    if s[i] == '(':
        stk.append('(')
        a+=1
        
    elif s[i] == ')':
        
        if stk:
            cnt+=1
            if stk[-1] == "(":
                cnt+= (a-b) +1
        stk.append(')')
        stk.pop(-1)
        stk.pop(-1)





        print(cnt)

print(cnt)
