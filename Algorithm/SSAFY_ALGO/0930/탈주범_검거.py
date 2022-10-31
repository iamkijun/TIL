import sys
sys.stdin = open('input.txt','r')

T = int(input())
def bfs(ci,cj):
    visited[ci][cj] = 1
    q =[]
    q.append([ci,cj])

    while q:
        ni,nj = q.pop(0)

        if visited[ni][nj] == L:
            return
        lens=0
        if arr[ni][nj] == 1:
            di=[-1,1,0,0]
            dj=[0,0,-1,1]
            lens =4
        elif arr[ni][nj] == 2:
            di = [-1,1]
            dj = [0,0]
            lens=2
        elif arr[ni][nj] == 3:
            di = [0, 0]
            dj = [-1, 1]
            lens = 2
        elif arr[ni][nj] == 4:
            di = [-1, 0]
            dj = [0, 1]
            lens = 2
        elif arr[ni][nj] == 5:
            di = [1, 0]
            dj = [0, 1]
            lens = 2
        elif arr[ni][nj] == 6:
            di = [1, 0]
            dj = [0, -1]
            lens = 2
        elif arr[ni][nj] == 7:
            di = [-1, 0]
            dj = [0, -1]
            lens = 2

        for dr in range(lens):
            if 0<=ni+di[dr]<N and 0<=nj+dj[dr]<N and not visited[ni+di[dr]][nj+dj[dr]]:
                q.append([ni+di[dr],nj+dj[dr]])
                visited[ni+di[dr]][nj+dj[dr]] = visited[ni][nj] + 1

for t in range(1,T+1):
    N,M,R,C,L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    men = arr[R][C]
    bfs(R,C)

    for val in visited:
        print(val)
    print()