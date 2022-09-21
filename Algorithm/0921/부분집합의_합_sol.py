import sys
sys.stdin = open('input.txt','r')

T = int (input())

def dfs(n, sm, cnt):
    global ans
    # [0] 종료조건 (n에 관련), 정답 관련 처리
    if n == N:
        if sm == K and cnt == N:
            ans +=1
        return
    
    dfs(n+1,sm+li[n],cnt+1)     #사용하는 경우
    dfs(n+1,sm,cnt)             #사용하지 않는 경우


for t in range(1,T+1):

    N, K = map(int, input().split())
    li = [x for x in range(1,13)]

    ans = 0

    dfs(0,0,0)

    print(f'#{t} {ans}')