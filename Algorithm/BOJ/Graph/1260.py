import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

N, M, V = map(int, input().split())

graph =[[0] * (N+1) for _ in range(N+1)]

# [0] 그래프 만들기
for _ in range(M):
    a, b = map(int, input().split())

    graph[a][b], graph[b][a] = 1, 1

visited = [0] * (N+1)

# [1] dfs 함수
def dfs(graph, v, visited):

    visited[v] = 1
    print(v,end=' ')

    for i in range(1,N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(graph,i,visited)
    
dfs(graph, V, visited)
print()

visited = [0] * (N+1)

# [2] bfs 함수
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v= queue.popleft()
        print(v,end=' ')

        for i in range(1,N+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1

bfs(graph, V, visited)
print()