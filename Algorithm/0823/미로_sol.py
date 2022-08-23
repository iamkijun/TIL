import sys
sys.stdin = open('input.txt','r')

def dfs(si,sj):
    stk = [] # 빈 스택

    visited[si][sj] = 1

    while True:
        #상하좌우 네 방향, 미방문하였고 길이라면(벽이 아니면)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = si+di, sj+dj

            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] != 1:
                stk.append((si,sj))

                si, sj = ni, nj
                visited[ni][nj] = 1
                break
        else:
            if stk:
                si,sj = stk.pop()
            else:
                break

def dfs_recur(si,sj):
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] != 1:
            visited[ni][nj] = 1
            dfs_recur(ni, nj)


T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr= [list(map(int,input())) for _ in range(N)]

    # [1] 출발지, 목적지 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    # [2] visited 배열 초기화 후 전체 방문 표시
    visited = [[0]*N for _ in range(N)]
    dfs_recur(si,sj)

    print(f'#{t} {visited[ei][ej]}')
    
    