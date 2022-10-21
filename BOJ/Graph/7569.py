import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

M, N, H = map(int, input().split())

def bfs():
    cnt = 0
    while q:
        h, i, j = q.popleft()
        arr_visited[h][i][j] = 1

        for dh,di,dj in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):

            nh, ni, nj = h+dh, i+di, j+dj

            if 0<=nh <H and 0<=ni < N and 0<=nj <M and arr[nh][ni][nj] == 0 and arr_visited[nh][ni][nj] == 0:
                q.append([nh,ni,nj])
                arr[nh][ni][nj] = arr[h][i][j] + 1
                arr_visited[nh][ni][nj] = 1

arr = []
arr_visited =[]

for _ in range(H):
    li = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    arr.append(li)
    arr_visited.append(visited)

q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append([h, i, j])

bfs()

all_tomato = 0
max_day = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                all_tomato = 1
            max_day = max(max_day, arr[h][i][j])

if all_tomato:
    print(-1)
else:
    print(max_day-1)
