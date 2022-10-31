import sys
sys.stdin = open("Backtracking/input.txt","r")

N, M = map(int,input().split())

li = list(map(int, input().split()))

li.sort()

ans = []
ans_list= []

def dfs():
    if len(ans) == M:
        temp = ' '.join(map(str,ans))
        if temp not in ans_list:
            ans_list.append(temp)
    
        return

    for val in li:
        if ans and ans[-1] <= val:
            ans.append(val)
            dfs()
            ans.pop()
        elif not ans:
            ans.append(val)
            dfs()
            ans.pop()

dfs()

for val in ans_list:
    print(val)