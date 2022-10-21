import sys
sys.stdin = open("Graph/input.txt","r")

def dfs(n,cnt):
    global ans
    
    cnt += 1
    visited[n] = 1

    if n == find_E:
        ans = cnt

    for i in graph[n]:
        if not visited[i]:
            dfs(i,cnt)

N = int(input())

find_S, find_E = map(int,input().split())

graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    graph[E].append(S)
    graph[S].append(E)

ans = -1
cnt = -1
dfs(find_S,cnt)

print(ans)