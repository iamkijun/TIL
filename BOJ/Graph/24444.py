
import sys
sys.stdin = open("Graph/input.txt","r")
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

graph = [[] for x in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt= 1

def bfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    cnt +=1
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for e in graph[v]:
            if not visited[e]:
                visited[e] = cnt
                cnt+=1
                queue.append(e)
    
for i in range(1,N+1):
    graph[i].sort()

bfs(graph, R, visited)

for i in range(1,N+1):
    print(visited[i])
