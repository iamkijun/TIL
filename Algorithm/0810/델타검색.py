import sys
sys.stdin = open("input.txt", "r")

T = int(input())

di = [0,0,-1,1] #상하좌우
dj = [-1,1,0,0]

for t in range(1,T+1):
    N = int(input())
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    total = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 1 <= ni < N+1 and 1 <= nj < N+1: #유효한 인덱스면
                    total += abs(arr[i][j] - arr[ni][nj])


    print(f'#{t} {total}')
