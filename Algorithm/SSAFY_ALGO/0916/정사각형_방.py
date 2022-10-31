import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0

    max_cnt = 0

    for i in range(N):
        for j in range(N):
            cnt = 1
            ni = i
            nj = j
            while True:
                for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
                    if 0<= ni + di <N and 0<= nj + dj < N and arr[ni][nj] + 1 == arr[ni+di][nj+dj]:
                        cnt += 1

                        ni += di
                        nj += dj
                        break
                else:
                    break

            if cnt > max_cnt:
                max_cnt = cnt
                max_num = arr[i][j]
            elif cnt == max_cnt:
                if arr[ni][nj] < max_num:
                    max_num = arr[i][j]


    print(f'#{t} {max_num} {max_cnt}')