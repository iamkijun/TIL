import sys
sys.stdin = open('Data_Structure/input.txt')

from collections import deque

def bfs(r,c,d):
    global cnt

    q = deque()
    q.append([r,c,d])
    visited[r][c] = 1
    cnt += 1

    while q:
        current_r, current_c, current_d = q.popleft()
        d_cnt = 0

        while d_cnt < 4:
            if current_d == 0:
                next_r, next_c = current_r, current_c

                if 0<=next_r<N and 0<=next_c<M and arr[next_r][next_c] != 1 and not visited[next_r][next_c]:
                    q.append([next_r,next_c,current_d])

                else:
                    current_d = (current_d + 1) % 4
                    d_cnt += 1
                    continue
            
        
        if d_cnt == 4:

            if (current_d + 2) % 4



N, M = map(int, input().split())

r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

visited = [[0]*M for _ in range(N)]

bfs(r,c,d)
