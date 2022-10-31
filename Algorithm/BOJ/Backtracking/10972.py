'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''
def dfs(idx,sm):
    global min_cnt
    global visited
    global cnt

    if visited == [1]*N:
        
        min_cnt = min(min_cnt,sm)
        
        return

    for j in range(N):
        if arr[idx][j] != 0 and not visited[j]:
            visited[j] = 1
            dfs(j,sm+arr[idx][j])
            visited[j] = 0
            


import sys
# input = sys.stdin.readline
sys.stdin = open("Backtracking/input.txt","r")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0]* N
cnt = []
min_cnt = 1000000*N

for idx in range(N):
    visited = [0]* N
    visited[idx]  
    dfs(idx,0)

print(min_cnt)