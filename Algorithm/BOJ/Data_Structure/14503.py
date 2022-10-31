from os import curdir
import sys
sys.stdin = open('Data_Structure/input.txt')

from collections import deque

# d => 0,3,2,1 순서로 돌아야한다.(좌->하->우->상)
di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(r,c,d):
    global cnt

    visited[r][c] = 1
    cnt += 1

    while True:
        flag = 0
        for _ in range(4):
            next_r= r+di[(d+3)%4]
            next_c= c+dj[(d+3)%4]

            d = (d+3)%4

            if 0<=next_r<N and 0<=next_c<M and arr[next_r][next_c] == 0 and not visited[next_r][next_c]:
                
                visited[next_r][next_c] = 1
                r = next_r
                c = next_c
                cnt +=1
                flag = 1
                break
    
        if flag == 0:       #네 방향 모두 청소되었을 때
            if arr[r-di[d]][c-dj[d]] == 1:   #후진했는데 벽으로 막혔을 때   
                print(cnt)
                break
            else:                           #후진 가능
                r = r - di[d]
                c = c - dj[d]


N, M = map(int, input().split())

r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

visited = [[0]*M for _ in range(N)]

bfs(r,c,d)
