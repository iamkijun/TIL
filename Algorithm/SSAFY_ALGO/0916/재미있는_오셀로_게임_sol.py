import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [[0] * (N+1) for _ in range(N)]

    mid = N//2
    arr[mid][mid] = arr[mid+1][mid+1] = 2
    arr[mid+1][mid] = arr[mid][mid+1] = 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d

        # 8방향 뻗어나가면서 범위 내(0: 끝, 같은돌: 후보 뒤집고 끝, 다른돌: 후보에 저장)
        for di, dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0.-1)):
            S = []      #후보 리스트 초기화
            for mul in range(1,N):
                ni, nj = si+di*mul, sj+dj*mul

                if 1<=ni<=N and 1<=nj<=N:       #범위 안
                    if arr[ni][nj] == 0:        #빈 곳
                        break
                    elif arr[ni][nj] == arr[si][sj]:    #다른돌
                        while S:
                            ti, tj = S.pop()
                            arr[ti][tj] = d
                        break
                    else:                       #다른 돌
                        S.append((ni,nj))
                else:                           #범위 밖
                    break

    black = 0
    white = 0

    for lst in arr:
        black += lst.count(1)
        white += lst.count(2)
    print(f'#{t} {black} {white}')