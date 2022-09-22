import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

ans = []

def dfs(n):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(n, N):
        if li[i] not in ans:
            ans.append(li[i])
            dfs(i)
            ans.pop()

dfs(0)