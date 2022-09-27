import sys
sys.stdin = open('input.txt','r')

T = int(input())

def check(si,sj):
    # [1]위쪽 체크
    for i in range(si):
        if arr[i][sj] == 1:
            return False

    # [2] 좌상 대각선 체크
    i, j = si - 1, sj - 1

    while i>=0 and j>=0:
        if arr[i][j]:
            return False
        i, j = i-1, j-1

    # [3] 우상 대각선 체크
    i, j = si - 1, sj + 1

    while i>=0 and j<N:
        if arr[i][j]:
            return False
        i, j = i - 1, j + 1

    return True


def dfs(n):
    global cnt

    if n==N:
        cnt += 1
        return

    for j in range(N):
        if check(n,j):
            arr[n][j] = 1
            dfs(n+1)
            arr[n][j] = 0

def dfs_tb1(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for j in range(N):
        if j not in v1 and (n+j) not in v2 and (n-j) not in v3:
            v1.append(j), v2.append(n+j), v3.append(n-j)
            dfs_tb1(n + 1)
            v1.pop(),v2.pop(),v3.pop()




for t in range(1,T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    cnt = 0

    # dfs(0)
    v1 = []
    v2 = []
    v3 = []

    dfs_tb1(0)

    print(f'#{t} {cnt}')