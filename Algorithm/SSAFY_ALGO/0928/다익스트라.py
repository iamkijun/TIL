import sys
sys.stdin = open('0928/input.txt','r')

INF = 500
def dijkstra(a):
    D = arr[a][::]
    visited = [0] * N
    visited[a] = 1

    for _ in range(N-1):
        #[1] 미방문 노드 가운데 최소거리 노드 번호 찾고 방문처리
        mn, i_min = INF, 0
        for i in range(N):
            if visited[i] == 0 and mn>D[i]:
                i_min, mn = i, D[i]
                visited[i] = 1

        #[2] 모든 노드 대상으로 최단거리 갱신
        for i in range(N):
            D[i] = min(D[i], D[i_min]+arr[i_min][i])
        
    return D[N-1]

T = int(input())

for t in range(1,T+1):
    N, E = map(int, input().split())
    
    arr = [[500]*N for _ in range(N)]
    
    for _ in range(E):
        start, end, weight = map(int, input().split())
        arr[start][end] = weight

    for i in range(N):
        arr[i][i] = 0

    ans = dijkstra(0)

    print(f'#{t} {ans}')