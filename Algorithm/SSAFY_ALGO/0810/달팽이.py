import sys
sys.stdin = open("input.txt", "r")

T = int(input())

di = [0,1,0,-1] #우하좌상
dj = [1,0,-1,0]

for t in range(1,T+1):
    N = int(input())
    if N ==1:
        print(f'#{t}')
        print(1)
        continue
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    val= 2
    dir =0
    ni, nj = 0, 0
    for i in range(N):
        for j in range(N):
            ni += di[dir]
            nj += dj[dir]

            if 0 <=ni < N and 0<=nj < N:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = val
                    val+=1
                elif arr[ni][nj] != 0:
                    ni -= di[dir]
                    nj -= dj[dir]
                    dir = (dir + 1) % 4
                    ni += di[dir]
                    nj += dj[dir]
                    arr[ni][nj] = val
                    val += 1
            else:
                ni -= di[dir]
                nj -= dj[dir]
                dir = (dir+1) % 4
                ni += di[dir]
                nj += dj[dir]
                arr[ni][nj] = val
                val += 1

            if val > N **2:
                break

    print(f'#{t}')
    for a in range(N):
        print(*arr[a])