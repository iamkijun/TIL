import sys
sys.stdin = open("Graph/input.txt","r")

from itertools import combinations
from copy import deepcopy
from collections import deque

def bfs(ci,cj):
    q = deque()
    q.append([ci,cj])

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(0,-1),(1,0),(0,1)):
            ni, nj = ci + di, cj + dj
        
            if 0<=ni<N and 0<=nj<M and temp_arr[ni][nj] == 0:
                temp_arr[ni][nj] = 2
                q.append([ni,nj])
                
                

    return

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

zeros = []
twos = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeros.append([i,j])
        elif arr[i][j] == 2:
            twos.append([i,j])
            
        
max_safe = 0

for a in combinations(zeros,3):
    temp_arr = deepcopy(arr)
    # 벽 세우기 (3개)
    temp_arr[a[0][0]][a[0][1]] = 1
    temp_arr[a[1][0]][a[1][1]] = 1
    temp_arr[a[2][0]][a[2][1]] = 1
    # 값 찾기
    
    for birus in twos:
        bfs(birus[0],birus[1])
        
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_arr[i][j] == 0:
                cnt +=1
    
    if cnt > max_safe:
        max_safe = cnt
        

print(max_safe)
