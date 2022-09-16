import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())
top = list(map(int, input().split()))
ans = [0] * N
stk = []

for i in range(N-1,0,-1):
    for j in range(i-1,-1,-1):
        
        if i>1 and max(top[:i-1]) <= top[i]:
            break
        
        if top[j] > top[i]:
            ans[i] = j+1
            break

print(*ans)