import sys
sys.stdin = open('input.txt','r')

N = int(input())

arr = [[1] * (N+1)] + [[1] + list(map(int, input().split())) for _ in range(N)]

HO = 0 #가로
VIR = 1 #세로
DIAG = 2 #대각

cnt = 0

def dfs(nowy, nowx, type):
    global cnt
    if (nowy, nowx) == (N, N):
        cnt += 1
        return

    #[1] 가로로 이동 가능한 경우
    if type == HO or type == DIAG:
        if nowx < N and arr[nowy][nowx+1] == 0:
            dfs(nowy, nowx+1, HO)

    #[2] 세로로 이동 가능한 경우
    if type == VIR or type == DIAG:
        if nowy < N and arr[nowy+1][nowx] == 0:
            dfs(nowy+1, nowx, VIR)

    #[3] 대각선으로 이동 가능한 경우
    if nowx< N and nowy< N:
        if arr[nowy+1][nowx] == 0 and arr[nowy][nowx+1] == 0 and arr[nowy+1][nowx+1] == 0:
            dfs(nowy+1, nowx+1, DIAG)


dfs(1, 2, HO)

print(cnt)
