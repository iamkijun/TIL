import sys
sys.stdin = open("Backtracking/input.txt","r")

def dfs():

    if len(li) == M:
        print(' '.join(map(str,li)))
        return
    
    for i in range(1,N+1):
        if i not in li:
            if not li:
                li.append(i)
                dfs()
                li.pop()
            elif li and i > li[-1]:
                li.append(i)
                dfs()
                li.pop()


N, M = map(int,input().split())

li = []

dfs()