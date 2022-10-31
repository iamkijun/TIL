import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for si in range(N): # +모양
        for sj in range(N): # 기준좌표 si, sj

            cnt = arr[si][sj]
            for m in range(1, M):
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = si+di*m, sj+dj*m
                    if 0<=ni<N and 0<=nj<N:
                        cnt += arr[ni][nj]
            if ans < cnt:
                ans =cnt

    for si in range(N):  # X모양
        for sj in range(N):  # 기준좌표 si, sj

            cnt = arr[si][sj]
            for m in range(1, M):
                for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    ni, nj = si + di * m, sj + dj * m
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if ans < cnt:
                ans =cnt

    print(f'#{t} {ans}')