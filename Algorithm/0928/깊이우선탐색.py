import sys
sys.stdin = open('0928/input.txt','r')

def dfs(graph, n, visited):
    
    visited[n] = 1
    print(n, end=' ')

    for val in graph[n]:
        if not visited[val]:
            dfs(arr, val, visited)

T = int(input())

for t in range(1,T+1):
    V, E = map(int ,input().split())

    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        a, b =map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # for i in range(1,V+1):
    #     arr[i].sort()
        
    print(f'#{t}', end=" ")
    dfs(arr, 1, visited)
    print()