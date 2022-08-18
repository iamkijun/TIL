import sys
sys.stdin = open("input.txt","r")
# [1] dfs stack
'''
def dfs(s):   #start 위치를 받는다
    stk = []

    visited[s] = 1
    
    while True:
        for e in adj[s]:
            if not visited[e]:
                stk.append(s)  # 더이상 갈 곳이 없을 때, 되돌아올 위치 push
                
                s = e
                visited[s] = 1
                break
        else:
            if stk:
                s = stk.pop() # 후퇴
            else:
                break # 끝까지 다 갔으니까 탈출
'''

# [2] dfs recursive
def dfs_recur(s):
    # 기준에서 연결된 방문 안한 노드 찾으면 방문
    for e in adj[s]:
        if not visited[e]:
            visited[e] = 1
            dfs_recur(e)


T = int(input())

for t in range(1,T+1):

    V, E = map(int, input().split())        # V : 노드 수, E : 간선 수

    adj = [[] for _ in range(V+1)]         #인접원소 리스트 생성

    for _ in range(E):
        s, e = map(int, input().split())       # s : 출발, e : 도착
        adj[s].append(e)       #단방향으로 연결 표시

    S, G = map(int, input().split())        # 출발지, 목적지

    visited = [0] * (V+1)           # 방문할 때 마다

    # dfs(S)
    dfs_recur(S)

    print(f'#{t} {visited[G]}')
