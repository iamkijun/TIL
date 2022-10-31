import sys
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]

    li = []
    for k in range(K):
        j, i = map(int, input().split())
        li.append([i,j])
        arr[i][j] = 1
        

    visited = [[0] * M for _ in range(N)]

    def bfs(i,j):
        q = deque()
        q.append([i,j])
        visited[i][j] = 1

        while q:
            ci,cj = q.popleft()

            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                ni, nj = ci + di, cj + dj

                if 0<= ni < N and 0<= nj < M and arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append([ni,nj])
        
        return

    cnt = 0 
    for val in li:
        if not visited[val[0]][val[1]]:
            bfs(val[0],val[1])
            cnt += 1

    print(cnt)