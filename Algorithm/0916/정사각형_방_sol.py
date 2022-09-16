import sys
sys.stdin = open('input.txt','r')

def BFS(si,sj):
    q = []
    ans = []

    q.append([si,sj])

    visited[si][sj] = 1

    ans.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
            ni, nj = ci+di, cj+dj
            # 범위 내
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and abs(arr[ci][cj]-arr[ni][nj]) == 1:
                q.append([ni,nj])
                visited[ni][nj] = 1
                ans.append(arr[ni][nj])

    return len(ans), min(ans)



T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 전체순회: 방문하지 않은 노드라면 방문
    visited = [[0]*N for _ in range(N)]

    cnt, num = 0, N*N
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tcnt, tnum = BFS(i,j)
                if tcnt > cnt:
                    cnt, num = tcnt, tnum
                elif tcnt == cnt and tnum < num:
                    cnt, num = tcnt, tnum

    print(f'#{t} {num} {cnt}')