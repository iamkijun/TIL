T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(N)]

    maxV=0

    for i in range(N):
        counth = 0

        for j in range(M):
            if a[i][j] == 1:
                counth +=1
                if maxV < counth:
                    maxV = counth
            else:
                counth = 0

    for i in range(M):
        countv = 0
        for j in range(N):
            if a[j][i] == 1:
                countv +=1
                if maxV < countv:
                    maxV = countv
            else:
                countv = 0

    print(f'#{t} {maxV}')