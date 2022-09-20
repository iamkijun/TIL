import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_count = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            count=0
            for k1 in range(M):
                for k2 in range(M):
                    count += arr[i+k1][j+k2]
            if count > max_count:
                max_count = count

    print(f'#{t} {max_count}')