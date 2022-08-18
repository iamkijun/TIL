import sys
sys.stdin = open("input.txt","r")

def DFS(v): # v : 시작 지점, N : 정점 개수
    # [1] 필요 자료 구조화
    visited = [0] * (V+1) # 방문한 노드 체크
    stk = [] # 스택(이전 탐색 지점)

    # [2] DPS 시작 작업
    s = v

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

    V, E = map(int, input().split())        # V : 노드 수, E : 간선 수

    adj = [[0] * (V+1) for _ in range(V+1)]         #인접원소 리스트 생성

    for _ in range(E):
        i, j = map(int, input().split())       # S : 출발 노드, G : 도착 노드
        adj[i][j] = adj[j][i] = 1       #양방향으로 연결 표시

    S, G = map(int, input().split())
    sols = []

    DFS(1)

    print(sols)

    if sols[-1] == V:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')