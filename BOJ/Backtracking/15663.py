import sys
sys.stdin = open("Backtracking/input.txt","r")

def dfs():

    if len(ans) == M:
        temp = ' '.join(map(str,ans))
        if temp not in total:
            total[temp] = 1
            return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i]= 1
            ans.append(li[i])
            dfs()
            ans.pop()
            visited[i]= 0


N, M = map(int,input().split())

li = list(map(int, input().split()))
li.sort()

ans = []
total = {}

visited = [0]*N

dfs()

for val in total:
    print(val)


