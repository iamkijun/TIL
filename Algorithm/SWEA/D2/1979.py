import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for t in range(1,T+1):
    N, K = map(int, input().split())
    arr = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]

    count =0

    for i in range(1,N+1):  
        for j in range(1,N-K+2):
            totalh= 0
            totalv= 0
            for k in range(K):
                totalv += arr[i][j+k]
                totalh += arr[j+k][i]

            if totalv == K:
                if arr[i][j-1] == 0 and arr[i][j+K] == 0:
                    count += 1

            if totalh == K:
                if arr[j-1][i] ==0 and arr[j+K][i] == 0:
                    count += 1
                
            
    
    print(f'#{t} {count}')
