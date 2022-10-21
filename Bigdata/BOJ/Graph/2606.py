import sys
sys.stdin = open("Graph/input.txt","r")

N = int(input())   # 컴퓨터의 수

nums = int(input())  # 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for x in range(N+1)] 
for i in range(nums):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
stk = []

def dfs(arr, v, visited):
    
    visited[v] = 1

    stk.append(v)
    
    for i in arr[v]:
        if visited[i] == 0:
            dfs(arr, i, visited)

    return stk

print(len(dfs(graph,1,visited))-1)