import sys
sys.stdin = open('input.txt','r')

def bfs(S,G):
    visited = [0] * (V+1)

    # q에 시작 노드 번호, 시작점으로부터의 거리
    q = [[S,0]]
    visited[S] = 1 #방문처리

    while q:
        c, d = q.pop(0) # 현재 노드번호(current의 c)
        if c == G:      # 종료조건: 목적지인 경우 거리(d) 반환
            return d
        for end in adjL[c]: #c와 연결된 노드 순서대로
            if not visited[end]:
                q.append([end,d+1]) #현재 노드까지의 거리 + 1
                visited[end] = 1

    # G가 연결된 노드가 아님
    return 0


T = int(input())
for t in range(1, T + 1):

    V, E = map(int,input().split())

    # 인접리스트에 연결된 노드 추가(양방향)
    adjL = [[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        adjL[s].append(e)
        adjL[e].append(s)
    S, G =map(int, input().split())         #S 출발노드, G 도착노드

    ans = bfs(S,G)

    print(f'#{t} {ans}')