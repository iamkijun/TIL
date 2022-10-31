import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int, input().split())

def dfs():
    if len(li) == M:
        print(' '.join(map(str, li)))
        return

    for i in range(1,N+1):
        try:
            if li[-1] <= i:
                li.append(i)
                dfs()
                li.pop()
        except:
            li.append(i)
            dfs()
            li.pop()


li = []

dfs()