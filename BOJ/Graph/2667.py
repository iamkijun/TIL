import sys
sys.stdin = open("Graph/input.txt","r")

N = int(input())

arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def cnts(ci,cj):
    global cnt

    q = []
    q.append([ci,cj])
    visited[ci][cj] = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == '1' and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt +=1
                q.append([ni,nj])


cnts_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            
            cnt = 1
            cnts(i,j)
            
            cnts_list.append(cnt)

            
            

cnts_list.sort()

print(len(cnts_list))
for val in cnts_list:
    print(val)

