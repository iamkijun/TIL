import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque

def bfs(ci,cj):
    global color
    q = deque()

    q.append([ci,cj])
    visited[ci][cj] = 1

    

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni,nj])


N = int(input())

arr = [list(input()) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
# for val in visited:
#     print(val)

# for val in arr:
#     print(val)

cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = arr[i][j]
            bfs(i,j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

cnt_rg = 0
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = arr[i][j]
            bfs(i,j)
            cnt_rg += 1

print(cnt, cnt_rg)