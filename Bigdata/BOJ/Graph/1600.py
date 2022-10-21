import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

K = int(input())
W, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]

def bfs(si,sj,n):
    q = deque()
    q.append([si,sj,n])
    visited = [[[0]*31 for _ in range(W)] for _ in range(H)]

    while q:
        ci, cj, n = q.popleft()

        # 최단거리 출력
        if ci == H-1 and cj == W-1:
            return visited[ci][cj][n]

        #모든 상황에서 상하좌우로 이동 가능
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W:
                if arr[ni][nj] == 0 and not visited[ni][nj][n]:
                    visited[ni][nj][n] = visited[ci][cj][n] + 1
                    q.append([ni,nj,n])

        #대각선으로 이동 가능한 경우
        if n>0:
            for di,dj in ((-2,1),(-2,-1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<H and 0<=nj<W:
                    if arr[ni][nj] == 0 and not visited[ni][nj][n-1]:
                        visited[ni][nj][n-1] = visited[ci][cj][n] + 1
                        q.append([ni,nj,n-1])

    #도착 못한경우
    return -1


print(bfs(0,0,K))
