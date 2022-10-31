import sys
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr_min = min(map(min, arr))    # min_height
arr_max = max(map(max, arr))    # max_height

def bfs(i, j):
    q = deque()

    q.append([i,j])

    visited[i][j] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] >= height and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni,nj])

ans = 0
for height in range(arr_min, arr_max + 1):
    visited = [[0]*N for _ in range(N)]

    cnt = 0            # 안전 영역의 개수
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= height and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
