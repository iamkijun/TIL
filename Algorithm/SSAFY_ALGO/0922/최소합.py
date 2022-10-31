import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(ci,cj, sm):
    global ans

    if sm > ans:
        return

    if ci == N and cj == N:
        ans = min(ans, sm)
        return

    #아래로 이동
    if ci < N:
        dfs(ci+1, cj, sm+arr[ci+1][cj])
    #오른쪽으로 이동
    if cj < N:
        dfs(ci, cj+1, sm+arr[ci][cj+1])




for t in range(1,T+1):
    N = int(input())

    arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 10*2*N-10

    ans = 10*2*N

    dfs(1,1,arr[1][1]) # 현재 x좌표, 현재 y좌표 현재 값

    print(f'#{t} {ans}')