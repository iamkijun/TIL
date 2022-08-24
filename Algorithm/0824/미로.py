import sys
sys.stdin = open('0824/input.txt','r')

def bfs(si,sj): #s: 시작좌표
    # [1] q 초기화
    q = []

    # [2] 초기 데이터들을 q에 삽입(+단위작업: visit표시)
    q.append([si,sj])
    visited[si][sj] = 1

    while q:    #q에 데이터가 있는 동안 반복
        si, sj = q.pop(0) #제일 앞에서 데이터를 꺼냄
        # 아래에 정답 코드 만들어보기

        if arr[si][sj] == 3:
            return 1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = si+di, sj+dj

            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni,nj])
                visited[ni][nj] = 1

    return 0

T = int(input())

for t in range(1, T + 1):

    N = int(input())

    arr= [list(map(int,input())) for _ in range(N)]

    # [1] 출발지, 목적지 찾기
    breakpoint =False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                breakpoint = True
                break
        if breakpoint:
            break
    

    # [2] visited 배열 초기화 후 전체 방문 표시
    visited = [[0]*N for _ in range(N)]    

    print(f'#{t} {bfs(si,sj)}')