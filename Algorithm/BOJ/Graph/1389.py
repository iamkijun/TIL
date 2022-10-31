import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

N, M = map(int,input().split())

def bfs(n):
    q = deque()
    q.append(n)
    
    visited[n] = 1

    while q:
        c = q.popleft()

        for i in graph[c]:
            if not visited[i]:
                visited[i] = visited[c] + 1
                q.append(i)
                


graph = [[] for _ in range(N+1)]

for _ in range(M):
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)

min_val = 500000
min_idx = 1
for i in range(1,N+1):
    cnt = 0
    visited = [0] * (N+1)
    bfs(i)
    bacon_num =sum(visited[1:])-(N-1)-visited[i]
    
    if bacon_num < min_val:
        min_val = bacon_num
        min_idx = i

print(min_idx)