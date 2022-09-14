import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# sys.stdin = open('Tree/input.txt','r')

N = int(input())

adj = [[] for _ in range(N+1)]

for i in range(2,N+1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (N+1)

ans = [0] * (N+1)

def dfs(adj,v,visited):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            ans[i] = v
            dfs(adj, i, visited)

dfs(adj,1,visited)


for i in range(2,N+1):
    print(ans[i])