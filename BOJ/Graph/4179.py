import sys
sys.stdin = open("Graph/input.txt","r")

def escape():

    while f_q:
        
        fi, fj = f_q.pop(0)

        for dr in range(4):
            ni, nj = fi+di[dr], fj+dj[dr]
            
            if 1<=ni<=R and 1<=nj<=C:
                if arr[ni][nj] != '#' and not fire_visited[ni][nj]:
                    f_q.append([ni,nj])
                    fire_visited[ni][nj] = fire_visited[fi][fj] + 1

    while j_q:
        
        ci, cj = j_q.pop(0)

        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]

            if 1<=ni<=R and 1<=nj<=C:
                if arr[ni][nj] != '#' and not visited[ni][nj]:
                    if not fire_visited[ni][nj] or fire_visited[ni][nj] > visited[ci][cj]+1:
                        j_q.append([ni,nj])
                        visited[ni][nj] = visited[ci][cj] + 1
            else:
                return visited[ci][cj]+1

    return 'IMPOSSIBLE'



R, C = map(int, input().split())

arr = [['A']*(C+2)] +[['A'] +list(input())+ ['A'] for _ in range(R)] +[['A']*(C+2)]

di =[-1,1,0,0]
dj =[0,0,-1,1]


ci,cj,fi,fj = -1,-1,-1,-1
j_q = []
f_q = []

for i in range(1,R+1):
    
    if 'J' in arr[i]:
        ci = i
        cj = arr[i].index('J')
        j_q.append([ci,cj])

    if 'F' in arr[i]:
        fi = i
        fj = arr[i].index('F')
        f_q.append([fi,fj])

    if j_q and f_q:
        break

visited = [[0] * (C+2) for _ in range(R+2)]
fire_visited = [[0] * (C+2) for _ in range(R+2)]

print(escape())