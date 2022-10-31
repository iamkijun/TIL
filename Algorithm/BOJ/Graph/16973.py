import sys
sys.stdin = open("Graph/input.txt","r")
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append([si,sj,0])
    visited[si][sj] = 1
    while q:
        ci,cj,cnt = q.popleft()

        if ci == fi and cj == fj:
            return cnt

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = ci+di, cj+dj
            
            if 1<=ni and ni+H-1<=N and 1<=nj and nj+W-1<=M and not visited[ni][nj] and is_wall(ni,nj):
                q.append([ni,nj,cnt+1])
    
    return -1

def is_wall(ci,cj):
    visited[ci][cj] = 1

    for i, j in walls:
        if ci<=i<ci+H and cj<=j<cj+W:
            return False

    return True



N, M = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

walls = []

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == 1:
            walls.append([i,j])
            
visited = [[0]*(M+1) for _ in range(N+1)]

H,W, si,sj, fi,fj = map(int, input().split())

print(bfs(si,sj))