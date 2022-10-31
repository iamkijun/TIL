import sys
sys.stdin = open('input.txt','r')

T= int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    cnt = 0 #농작물 개수 세는 변수 선언

    for i in range(N):
        # [1] 처음부터 절반까지
        if i <= N//2:
            for k in range(2*i+1):  # 2*i+1 <- 셀 개수
                cnt += arr[i][N//2-i:N//2+i+1][k]   # N//2-i 시작점, N//2+i+1 끝점 전부 다 count

        # [2] 절반 이후부터 끝까지
        else:
            for k in range(2*(N-i-1)+1):   # 2*(N-i-1)+1 <- 셀 개수
                cnt += arr[i][N//2-(N-i-1):N//2+((N-i-1)+1)][k]     # N//2-(N-i-1) 시작점, N//2 + (N-i-1) + 1 끝점 전부 다 count

    print(f'#{t} {cnt}')


