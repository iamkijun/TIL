
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("Graph/input.txt","r")

N,M,R = map(int, input().split())

visited= [0] * (N+1)
graph = [[] for x in range(N+1)]
cnt = 1
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    cnt+=1
    for e in graph[v]:
        if visited[e] == 0:
            visited[e] = cnt
            dfs(graph, e, visited)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

dfs(graph, R, visited)

for i in range(1,N+1):

    print(visited[i])
