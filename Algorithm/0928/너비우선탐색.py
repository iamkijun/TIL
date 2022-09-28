import sys
sys.stdin = open('0928/input.txt','r')

T = int(input())

def bfs(graph, n, visited):
    q = []
    q.append(n)
    visited[n] = 1

    while q:
        temp = q.pop(0)

        print(temp, end=" ")
        for val in graph[temp]:
            if not visited[val]:
                q.append(val)
                visited[val] = 1

for t in range(1,T+1):
    V, E = map(int ,input().split())

    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        a, b =map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1,V+1):
        arr[i].sort()
        
    print(f'#{t}', end=" ")
    bfs(arr,1,visited)
    print()