import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N = int(input())

    arr = [[-1] * (N+2)] + [[-1] + [0]*N + [-1] for _ in range(N)] + [[-1] * (N+2)]

    num = 1
    i = 1   #시작점x좌표
    j = 0   #시작점y좌표
    ni = 0  #di[0] - 초기 방향 우측
    nj =1   #dj[0]

    di = [0,1,0,-1] #우 하 좌 상
    dj = [1,0,-1,0]

    d = 0 #di,dj의 inddex
    
    while num <= N**2:

        if arr[i + ni][j + nj] == 0:
            i = i+ ni
            j = j+ nj
            arr[i][j] = num
            num+=1

        else:
            d = (d+1) % 4
            ni = di[d]
            nj = dj[d]
            i = i+ ni
            j = j+ nj
            arr[i][j] = num
            num+=1

    # 출력
    print(f'#{t}')
    for i in range(1,N+1):
        print(*arr[i][1:-1])