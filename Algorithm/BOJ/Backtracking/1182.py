import sys
# input = sys.stdin.readline
sys.stdin = open("Backtracking/input.txt","r")

N, S = map(int,input().split())

li = list(map(int,input().split()))

count = 0

def dfs(idx,val):
    global count

    if idx == N:
        return
            
    val += li[idx]
    if val == S:
        count += 1

    dfs(idx+1,val)
    dfs(idx+1,val-li[idx])

dfs(0,0)

print(count)