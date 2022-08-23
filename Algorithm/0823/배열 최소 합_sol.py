import sys
sys.stdin = open('input.txt','r')

def dfs(n,sm): #n:시작, sm: 합
    global ans

    if sm >= ans:
        return

    #종료조건 설정
    if n == N:
        if ans > sm:
            ans = sm
        return

    #열의 개수 만큼 돌리기
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm+arr[n][j])
            visited[j] = 0

T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N #열의 개수만큼 필요

    ans = 10 * N

    dfs(0,0)        # n==0 (0행), sum =0

    print(f'#{t} {ans}')

