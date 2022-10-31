import sys

sys.stdin = open('input.txt', 'r')

def bfs(si,sj,ei,ej):
    # [1] 초기 데이터들을 q에 삽입(+단위작업: visit표시)
    q = [[si,sj]]

    # [2] visited 배열 초기화 후 전체 방문 표시
    # visited = [[0] * 16 for _ in range(16)]
    visited = [[1] * 16] + [[1] + [0] * 14 + [1] for _ in range(14)] + [[1] * 16]

    while q:
        si, sj = q.pop()

        if arr[si][sj] == arr[ei][ej]:
            return 1

        # 4방향 범위 내 안가본 길이면 방문
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우 방문
            ni, nj = si + di, sj + dj

            #범위 내, 아직 가보지 않았고, 벽이 아니면(1이 아니면) 방문
            if 1 <= ni < 15 and 1 <= nj < 15 and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return 0



T =10
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

                        #시작점
    for i in range(16):
        if 2 in arr[i]:
            for j in range(16):
                if arr[i][j] == 2:
                    si, sj = i, j       #끝점
        if 3 in arr[i]:
            for j in range(16):
                if arr[i][j] == 3:
                    ei, ej = i, j       #끝점

    ans = bfs(si,sj,ei,ej)

    print(f'#{t} {ans}')
