import sys
sys.stdin = open('Backtracking/input.txt','r')

di = [1,-1,0,0]
dj = [0,0,1,-1]

def dfs(x,y,cnt, ans):
    if cnt == K:
        global max_val
        max_val = max(ans,max_val)
        return

    for i in range(1,N+1):
        for j in range(1,M+1):
            
            if visited[i][j]:
                continue
        
            for x in range(4):
                ni,nj = i+di[x], j+dj[x]
                if 1<=ni<=N and 1<=nj<=M and visited[ni][nj]:
                    break
            
            else:
                visited[i][j] = True
                dfs(i,j,cnt+1,ans+arr[i][j])
                visited[i][j] = False

N,M,K = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

visited = [[False] * (M+1) for _ in range(N+1)]
max_val = -10000*K

dfs(1,1,0,0)
print(max_val)