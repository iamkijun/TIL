import sys
sys.stdin = open('input.txt','r')

def bfs(s): #s: 시작점
    global sols
    # [1] q, visited, 필요한 flag 초기화
    q = []
    visited = [0] * (V+1)
    sols = []

    # [2] 초기 데이터들을 q에 삽입(+단위작업: visit표시)
    q.append(s)
    visited[s] = 1
    sols.append(s)

    while q:    #q에 데이터가 있는 동안 반복
        s = q.pop(0) #제일 앞에서 데이터를 꺼냄
        # 아래에 정답 코드 만들어보기


        # [3] 4, 8방향, 연결된 노드, ...안가본, 조건에 맞는 곳이면
        for e in range(1, V+1):
            if not visited[e]:
                q.append(e)
                visited[e] = 1
                sols.append(e)

T = int(input())
for t in range(1, T + 1):

    V, E = map(int,input().split())

    bfs(1)      #시작지점 1, 방문순서대로 sols에 추가

    print(f'#{t}', *sols)