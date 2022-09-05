import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())
top = list(map(int, input().split()))
ans = [0] * N
stk = [[top[-2],N-2]]

for i in range(N-1,0,-1):
    while stk:
        if stk[-1][0] <= top[i]:
            tem = stk.pop()
            ans[i] = tem[1]+1
        else:
            stk.append([top[i],i])
    print(stk,ans)

print(*ans)