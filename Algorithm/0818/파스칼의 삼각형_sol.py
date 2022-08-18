import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [[0] * (N+1) for _ in range(N+1)]

    arr[1][1] = 1 #초기값 설정

    for i in range(2,N+1):
        for j in range(1,i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]



    print(f'#{t}')
    for k in range(1,N+1):
        for j in range(1, k + 1):
            print(arr[k][j], end=' ')
        print()
