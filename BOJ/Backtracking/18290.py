import sys
sys.stdin = open('Backtracking/input.txt','r')

N,M,K = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

visited = [[0] * (M+1) for _ in range(N+1)]
max_val = 0

def dfs(x,j,cnt, ans):
    global max_val

    if cnt == K:
        if ans > max_val:
            max_val = ans
        return

    for i in range(1,N+1):
        for j in range(1,M+1):

            if visited[i][j] == 0:
                continue
        
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni = i+di
                nj = j+dj
                if 1<=ni<=N and 1<=nj<=M and visited[ni][nj]:
                    break
            else:
                visited[i][j] = 1
                dfs(i,j,cnt+1,ans+arr[i][j])
                visited[i][j] = 0

dfs(0,0,0,0)

print(max_val)