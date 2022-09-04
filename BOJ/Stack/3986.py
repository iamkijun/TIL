import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())

ans = 0

for n in range(N):
    
    S = input()
    stk = []
    
    bp = 0
    for val in S:
        if stk and stk[-1] == val:
            stk.pop()
        else:
            stk.append(val)
    
    if stk:
        pass
    else:
        ans +=1
print(ans)