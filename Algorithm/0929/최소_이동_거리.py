import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n,cnt):
    global min_val

    if cnt >= min_val:
        return

    if n == N:
        min_val = cnt
        return

    for i in range(N+1):
        if arr[n][i] != 0 and not visited[i]:
            visited[i] = 1
            cnt +=arr[n][i]
            dfs(i,cnt)
            cnt -=arr[n][i]
            visited[i] = 0


for t in range(1,T+1):
    N, E = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]

    for i in range(E):
        s, e, w = map(int,input().split())
        arr[s][e] = w

    min_val = 10*N
    visited = [0] * (N+1)
    visited[0] = 1
    dfs(0,0)

    print(f'#{t} {min_val}')