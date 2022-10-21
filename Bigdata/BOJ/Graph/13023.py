import sys
sys.stdin = open("Graph/input.txt","r")

N, M = map(int, input().split())

arr = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, n):
    global cnt
    if n == 4:
        cnt = 1
        return

    for i in arr[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i,n+1)
            visited[i] = 0

cnt = 0
for i in range(N):
    visited[i] = 1
    dfs(i,0)
    visited[i] = 0
    if cnt == 1:
        break

print(cnt)