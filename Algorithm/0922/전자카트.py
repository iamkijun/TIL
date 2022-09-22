import sys
sys.stdin = open('input.txt','r')

def dfs(n,sm,s):
    global ans
    if sm >= ans:
        return

    if n == N-1:
        ans = min(ans,sm+arr[s][1])
        return

    for j in range(2,N+1):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm+arr[s][j], j)
            visited[j] = 0

T = int(input())

for t in range(1,T+1):

    N = int(input())

    arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N+1)
    ans = 100 * N #최대값을 초기값으로
    visited[1] = 1
    # 방문한 도시수 0, 배터리 합 0, 시작 구역 번호 1
    dfs(0,0,1)

    print(f'#{t}',ans)