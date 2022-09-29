import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n,first):
    global chance
    if first <= chance:
        return

    if n==N:
        chance = first
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, first*(arr[n][j]*0.01))
            visited[j] = 0          #여기까지 왔다는거는 실패했다는 뜻이니까 방문했던 방 되돌아오기


for t in range(1,T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    # 초기 확률 세팅
    chance = 100
    for i in range(N):
        chance *= (arr[i][i]*0.01)

    dfs(0, 100)

    print(f'#{t} {chance:.6f}')