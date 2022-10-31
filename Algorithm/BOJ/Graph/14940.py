import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j] = 0

    while q:
        ci,cj = q.popleft()

        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M:
                # if arr[ni][nj] == 0:
                #     visited[ni][nj] = 0
                if arr[ni][nj] == 1 and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append([ni,nj])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i,j)

for val in visited:
    print(*val)