import sys
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque

def bfs(si,sj):
    queue = deque()
    queue.append([si,sj])
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.popleft()
        
        for di, dj in ((-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)):
            ni = ci + di
            nj = cj + dj
            
            if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append([ni,nj])

while True:
    w, h = map(int, input().split())

    if w == 0 or h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0]* w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    
    print(cnt)