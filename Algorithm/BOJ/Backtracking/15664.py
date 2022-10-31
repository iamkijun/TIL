import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

ans = []

total = {}

visited = [0] * N

def dfs(n):
    if len(ans) == M:
        temp = ' '.join(map(str,ans))
        
        if temp not in total:
            total[temp] = 1
            print(temp)

        return
    
    for i in range(n,N):
        if not visited[i]:
            ans.append(li[i])
            visited[i] = 1
            dfs(i)
            visited[i] = 0
            ans.pop()

dfs(0)