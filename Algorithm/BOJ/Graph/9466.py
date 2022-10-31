import sys
sys.stdin = open("Graph/input.txt","r")

T = int(input())

def dfs(i):
    global ans
    visited[i] = 1
    temp.append(i)
    
    if visited[li[i]]:
        if li[i] in temp:
            ans += temp[temp.index(li[i]):]
    else:
        dfs(li[i])

for t in range(T):
    n = int(input())
    li = [0] + list(map(int,input().split()))

    visited = [0] * (n+1)
    ans = []

    for i in range(1,n+1):
        if not visited[i]:
            temp = []
            dfs(i)
            
    print(n - len(ans))
