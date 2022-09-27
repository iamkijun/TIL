import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n,sm):
    global ans

    if ans < sm:
        return

    if n==N:
        if sm < ans:
            ans=sm
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, sm+arr[n][j])
            visited[j] = 0          #여기까지 왔다는거는 실패했다는 뜻이니까 방문했던 방 되돌아오기

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 99 * N
    visited = [0] * N

    dfs(0, 0)

    print(f'#{t} {ans}')

