import sys
sys.stdin = open("Graph/input.txt","r")

input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())

def bfs(graph,v):
    visited = [0] * (N+1)
    visited[v] = 1
    cnt = 0
    queue = deque([v])

    while queue:
        v = queue.popleft()

        for e in graph[v]:
            if visited[e] == 0:
                queue.append(e)
                cnt+=1
                visited[e] == 1
    
    return cnt

graph = [[] for x in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []
max_cnt = 1

for i in range(1,N+1):
    cnt = bfs(graph,i)
    if cnt > max_cnt:
        max_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == max_cnt:
        ans.append(i)

print(*ans)

