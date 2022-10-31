import sys
sys.stdin = open("Graph/input.txt","r")

T = int(input())

def dfs(n):
    stk =[]
    visited = [0] *(V+1)

    s= n
    visited[s] = 1
    ans.append(s)
    
    while True:
        for i in range(1,V+1):
            if visited[i] == 0 and arr[s][i] == 1:
                stk.append(s)

                s = i
                visited[i] = 1
                ans.append(i)
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break
    

for t in range(1,T+1):
    V,E = map(int, input().split())
    arr =[[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        arr[s][e] = arr[e][s] = 1

    ans = []

    dfs(1)

    print(f'#{t}', *ans)