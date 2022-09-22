import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int,input().split())

li = list(map(int, input().split()))
li.sort()
ans = []

def dfs():
    if len(ans) == M:
        print(' '.join(map(str,ans)))
        return

    for val in li:
        ans.append(val)
        dfs()
        ans.pop()

dfs()