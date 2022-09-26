import sys
sys.stdin = open('input.txt')

T= int(input())

di=[1,1,-1,-1,1]
dj=[-1,1,1,-1,1]

def dfs(n,ci,cj,visited):
    global ans, si,sj

    if n==2 and ans>=len(visited)*2:
        return

    if n>3:
        return

    if n == 3 and (ci,cj) == (si,sj) and ans < len(visited):
        ans = len(visited)
    
    for dr in range(n, n+2):
        ni, nj = ci+di[dr], cj+dj[dr]
        if 0<= ni <N and 0<= nj <N and arr[ni][nj] not in visited:
            visited.append(arr[ni][nj])
            dfs(dr, ni, nj, visited)
            visited.pop()

for t in range(1,T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for si in range(N):
        for sj in range(N):
            visited= []
            dfs(0,si,sj,visited)

    print(f'#{t} {ans}')