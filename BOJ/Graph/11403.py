import sys
sys.stdin = open("Graph/input.txt","r")

N = int(input())

arr =[list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

def dfs(i):

    for val in graph[i]:
        if not visited[val]:
            visited[val] = 1
            dfs(val)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            graph[i].append(j)
            # graph[j].append(i)

# for val in arr:
#     print(val)

new = []

# print(graph)

for i in range(N):
    visited =[0] * (N)
    # visited[i] = 1
    dfs(i)
    
    new.append(visited)

for val in new:
    print(*val)
