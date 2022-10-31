import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1] =2
    arr[N//2-1][N//2] =1
    arr[N//2][N//2-1] =1
    arr[N//2][N//2] =2

    for _ in range(M):
        x, y, color = map(int, input().split())

        arr[y-1][x-1] = color

        #[1] 가로
        if (color+1)%2 in arr[y-1]:

        #[2] 세로

        print(arr)
