import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

ans = []
total = {}

def dfs():
    if len(ans) == M:
        temp = ' '.join(map(str,ans))
        if temp not in total:
            print(temp)
            total[temp] = 1
        return

    for i in range(N):

        ans.append(li[i])
        dfs()
        ans.pop()

dfs()