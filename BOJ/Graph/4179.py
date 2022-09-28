import sys
sys.stdin = open("Graph/input.txt","r")
'''
4 4
####
#JF#
#..#
#..#

걸린 시간: 2520ms
'''

def escape():

    while f_q:  #불지르기 먼저
        
        fi, fj = f_q.pop(0)

        for dr in range(4):
            ni, nj = fi+di[dr], fj+dj[dr]
            
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] != '#' and not fire_visited[ni][nj]: #벽이 아니고, 아직 불을 안질렀다면
                    f_q.append([ni,nj])
                    fire_visited[ni][nj] = fire_visited[fi][fj] + 1 # 몇 초 후에 불이 번졌는지

    while j_q:  #불 다 지른 후, 탈출 시작!
        
        ci, cj = j_q.pop(0)

        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]

            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] != '#' and not visited[ni][nj]:                                  #벽이 아니고, 아직 방문하지 않았다면
                    if not fire_visited[ni][nj] or fire_visited[ni][nj] > visited[ci][cj]+1:    #불이 아예 번지지 않은 곳이거나, 불이 번진 것보다 내가 더 일찍 도착할 경우 진행
                        j_q.append([ni,nj])
                        visited[ni][nj] = visited[ci][cj] + 1
            else:
                return visited[ci][cj]+1                                                        # 범위 밖으로 나갈 수 있을때: 미로에서 탈출했을 때 종료

    return 'IMPOSSIBLE'             #가능한 모든 곳을 방문했으나 탈출하지 못했을 경우

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

di =[-1,1,0,0]
dj =[0,0,-1,1]

j_q = []
f_q = []

for i in range(R):
    
    if 'J' in arr[i]:
        ci = i
        cj = arr[i].index('J')
        j_q.append([ci,cj])

    if 'F' in arr[i]:
        fi = i
        fj = arr[i].index('F')
        f_q.append([fi,fj])

visited = [[0] * C for _ in range(R)]
fire_visited = [[0] * C for _ in range(R)]

print(escape())

'''
걸린시간: 400ms
from collections import deque
n,m = map(int,input().split())
miro = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

q = deque()
for i in range(n):
    for j in range(m):
        if miro[i][j]=='J':
            q.append((i,j,'J'))
            visited[i][j]=1
        elif miro[i][j]=='F':
            q.appendleft((i,j,'F'))
            visited[i][j]=1

while q:
    x,y,state = q.popleft()
    if state=='J' and (x==n-1 or x==0 or y==m-1 or y==0):
        print(visited[x][y])
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and miro[nx][ny]!='#':
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny,state))
else: print("IMPOSSIBLE")
'''