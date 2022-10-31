import sys
sys.stdin = open("0817/input.txt","r")

def DFS(start):
    # [1] stk 등 필요 자료 구조 초기화
    stk = []
    visited = [0] * (V+1)

    # [2] DFS 시작 작업

    s = start

    visited[s] = 1
    sols.append(s)

    while True:
        for e in range(1, V+1):
            # s와 연결되고, 안가본곳
            if visited[e] == 0 and adj[s][e] == 1:
                # 돌아온 곳을 push
                stk.append(s)
                s = e
                visited[e] = 1
                sols.append(e)
                break
        else: #현재 s를 기준으로 방문 가능한 곳이 없음!
            if stk:
                s = stk.pop()
            else: # stack empty
                break


T = int(input())

for t in range(1,T+1):

    V, E = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]
    
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = adj[j][i] = 1 #양방향

    sols = []

    DFS(1)

    print(f'#{t}', *sols)
