import sys
sys.stdin = open("D3/input.txt","r")

T = int(input())

for t in range(1,T+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    total = 0

    for i in range(N):
        if i <= N//2:
            for val in arr[i][N//2-i:N//2+i+1]:
                total += val
            
        else:
            for val in arr[i][N//2-N+1+i:N//2+N-i]:
                total += val
        
    print(f'#{t} {total}')