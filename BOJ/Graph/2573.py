import sys
sys.stdin = open("Graph/input.txt","r")

from collections import deque

def melting(i,j):
    cnt = 0
    for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni, nj = i+di, j+dj
        if arr[ni][nj] == 0:
            cnt += 1
    return cnt

def bfs(i,j,num,visited):
    q = deque()
    q.append([i,j])
    visited[i][j] = num

    while q:
        #행, 열, 
        si, sj = q.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
            #범위 내
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] != 0 and not visited[ni][nj]:
                    visited[ni][nj] = num
                    q.append([ni,nj])

    return

def find_chunk(arr):
    
    chunk_nums = 0
    group_num = 2

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                cnt = bfs(i,j,group_num,visited)
                chunk_nums += 1
                group_num +=1
    
    return chunk_nums

N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
cnt= 1
while True:
    new_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                around = melting(i,j)
                if arr[i][j] - around <= 0:
                    new_arr[i][j] = 0
                else:
                    new_arr[i][j] = arr[i][j] - around
    arr = new_arr

    visited = [[0] * M for _ in range(N)]
    chunk_num = find_chunk(arr)

    if chunk_num == 0:
        cnt = 0
        break
    elif chunk_num >=2:
        break
    elif chunk_num ==1:
        cnt +=1

print(cnt)