import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n):
    global ans
    if n == N:
        ans = max(ans,int("".join(li)))
        return

    for i in range(len(li)-1):
        for j in range(i+1, len(li)):

            li[i],li[j] = li[j],li[i]
            temp = int(''.join(li))
            if visited.get((n,temp),1):       #해당 key값이 없는 경우 실행 - > True
                dfs(n+1)
                visited[(n,temp)] = 0

            li[i], li[j] = li[j], li[i]



for t in range(1,T+1):

    li, N = input().split()
    N = int(N)
    li = list(li)

    ans = 0
    visited = {}
    dfs(0)

    print(f'#{t}',ans)
