import sys
sys.stdin = open('input.txt','r')
'''
0100
1110
1011
1010
'''
T = int(input())
INF = 100 * 100 * 10
def bfs(ci, cj):

    q = [[ci,cj]]
    visited[ci][cj] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and visited[ni][nj]>visited[ci][cj]+arr[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                q.append([ni,nj])


for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    visited = [[INF]*N for _ in range(N)]

    bfs(0,0)

    print(f'#{t} {visited[N-1][N-1]}')