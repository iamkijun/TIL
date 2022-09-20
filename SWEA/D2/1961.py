import sys
sys.stdin = open("D2/input.txt")

T = int(input())

for t in range(1,T+1):

    N = int(input())

    arr = [list(map(str, input().split())) for _ in range(N)]

    new = [['']* 3 for _ in range(N)]

    for i in range(N):
        for j in range(3):
            for k in range(N):
                if j == 0:
                    new[i][j] += arr[N-k-1][i]
                elif j == 1:
                    new[i][j] += arr[N-i-1][N-k-1]
                elif j == 2:
                    new[i][j] += arr[k][N-i-1]
    print(f'#{t}')
    for n in range(N):
        print(*new[n])