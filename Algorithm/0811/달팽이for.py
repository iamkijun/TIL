import sys
sys.stdin = open("input.txt","r")

di=[0,1,0,-1]
dj=[1,0,-1,0]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i, j = 0, -1
    dir = 0
    cnt = 0

    while cnt <= N*N:
        ni, nj = i+di[dir], j+dj[dir] # 이동할 좌표 계산
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            i, j = ni, nj #현재 좌표 계산
            arr[i][j] = cnt
            cnt += 1
        else: # 불가능한 경우 => 방향 전환 후 기록
            dir = (dir+1) % 4

    print(f'#{t}')
    for li in arr:
        print(*li)