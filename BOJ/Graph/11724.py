import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("Graph/input.txt","r")

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
    graph[A].append(B)

visited =[False] * (N+1)

def dfs(v):
    visited[v] = True

    for e in graph[v]:
        if not visited[e]:
            dfs(e)

cnt =0

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)