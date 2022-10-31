import sys
sys.stdin = open('input.txt','r')

cost = [k*k + (k-1)*(k-1) for k in range(40)]

def bfs(i,j):
    global ans
    #초기값 세팅
    q = []
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    q.append((i,j))
    visited[i][j] = 1
    cnt += arr[i][j]      # 시작 위치에 집이 있는 경우 1 추가하고 bfs 시작

    while q:
        ci, cj = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):       #네방향 범위내에 안가본 곳이면 q 삽입
            ni, nj = ci+di, cj+dj
            #범위 내이고 방문하지 않았던 곳이라면
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:

                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] +1

                if arr[ni][nj] == 1:        #집이 있는 경우
                    cnt +=1

                    if cost[visited[ni][nj]] <= cnt * M and ans<cnt:
                        ans = cnt

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(N):      #모든 시작위치
            bfs(i, j)

    print(f'#{t} {ans}')