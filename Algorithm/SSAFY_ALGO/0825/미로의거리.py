import sys

sys.stdin = open('input.txt', 'r')


def bfs(si, sj, ei, ej):  # s: 시작좌표
    # [1] q 초기화
    q = []

    # [2] 초기 데이터들을 q에 삽입(+단위작업: visit표시)
    q.append([si, sj]) #si,sj:시작 좌표, 0: 걸어간 길이
    visited[si][sj] = 0

    while q:  # q에 데이터가 있는 동안 반복
        si, sj = q.pop(0)  # 제일 앞에서 데이터를 꺼냄

        if arr[si][sj] == arr[ei][ej]:
            return visited[ei][ej] -1

        #4방향 범위 내 안가본 길이면 방문
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하좌우 방문
            ni, nj = si + di, sj + dj
            # 범위 내 and 안가봤고 and 벽이 아니면 방문
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] += visited[si][sj] + 1

    return 0

T = int(input())

for t in range(1, T + 1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    # [1] 출발지, 목적지 찾기

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    # [2] visited 배열 초기화 후 전체 방문 표시
    visited = [[0] * N for _ in range(N)]

    ans = bfs(si, sj, ei, ej)

    print(f'#{t} {ans}')
