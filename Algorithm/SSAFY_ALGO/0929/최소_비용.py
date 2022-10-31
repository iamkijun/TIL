import sys
sys.stdin = open('input.txt','r')

from collections import deque

T = int(input())

di = [1,0,-1,0]
dj = [0,1,0,-1]
INF = 100* 200
def bfs(si,sj):
    q =deque()
    q.append([si,sj])
    s = [[INF] * N for _ in range(N)]
    s[si][sj] = 0

    while q:
        ci, cj = q.popleft()  # 중복 방문 가능  -> q empty 될때까지 작동

        for dr in range(4):
            ni,nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<N and s[ni][nj] > s[ci][cj]+1+max([0,arr[ni][nj]-arr[ci][cj]]):
                s[ni][nj] = s[ci][cj] + 1 + max(0,arr[ni][nj]-arr[ci][cj])
                q.append([ni,nj])

    return s[N-1][N-1]

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(0,0)

    print(f'#{t} {ans}')