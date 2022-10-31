import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())
A_list = list(map(int, input().split()))
ans = [-1] * N

stk = [[A_list[0],0]]

for i in range(1,N):
    while stk:
        if stk[-1][0] < A_list[i]:
            tem = stk.pop()
            ans[tem[1]] = A_list[i]
        else:
            break
    stk.append([A_list[i],i])

    print(stk,ans)

print(*ans)