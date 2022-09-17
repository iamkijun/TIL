import sys
sys.stdin = open('Tree/input.txt','r')

T = int(input())

def dfs(graph, v, visited):
    global cnt
    visited[v] = 1

    for val in graph[v]:
        if not visited[val]:
            cnt += 1
            dfs(graph,val,visited)

    


for t in range(1,T+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    cnt = 0
    visited = [0] * (N+1)

    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(graph,1,visited)

    print(cnt)
