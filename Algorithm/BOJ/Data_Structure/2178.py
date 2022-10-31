import sys

sys.stdin = open('Data_Structure/input.txt','r')

N, M = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int,input())) for _ in range(N)]

visited =[[0]*(M+1) for _ in range(N+1)]

ans = N*M

def bfs(si,sj):
    global ans


    q = []
    q.append([si,sj])
    visited[si][sj] = 1

    while q:
        
        ci, cj = q.pop(0)

        if ci == N and cj == M:
            return
        
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj

            if 0<ni<=N and 0<nj<=M and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = visited[ci][cj] +1
                q.append([ni,nj])

bfs(1,1)
# for val in visited:
#     print(val)
print(visited[N][M])


