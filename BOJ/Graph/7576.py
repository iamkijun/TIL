import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

#가로, 세로
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        ci,cj = q.popleft()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] ==0:
                    arr[ni][nj] += arr[ci][cj]+1
                    q.append([ni,nj])

    return

bfs()

max_val = 0

for val in arr:
    if 0 in val:
        max_val = 0
        break
    else:
        max_val = max(max(val),max_val)

print(max_val-1)