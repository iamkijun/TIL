'''
NASA에서는 화성 탐사를 위해 화성에 무선 조종 로봇을 보냈다. 실제 화성의 모습은 굉장히 복잡하지만,
로봇의 메모리가 얼마 안 되기 때문에 지형을 N×M 배열로 단순화 하여 생각하기로 한다.

지형의 고저차의 특성상, 로봇은 움직일 때 배열에서 왼쪽, 오른쪽, 아래쪽으로 이동할 수 있지만, 위쪽으로는 이동할 수 없다.
또한 한 번 탐사한 지역(배열에서 하나의 칸)은 탐사하지 않기로 한다.

각각의 지역은 탐사 가치가 있는데, 로봇을 배열의 왼쪽 위 (1, 1)에서 출발시켜 오른쪽 아래 (N, M)으로 보내려고 한다.
이때, 위의 조건을 만족하면서, 탐사한 지역들의 가치의 합이 최대가 되도록 하는 프로그램을 작성하시오.

5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15
'''

import sys
sys.stdin = open('DP/input.txt','r')

def dfs(si,sj):
    global cnt

    if si == N and sj == M:
        if cnt >= max_val:
            max_val = cnt
        return

    # 좌/우/하 이동
    for di, dj in ((0,-1),(0,1),(-1,0)):
        ni, nj = si+di, sj+dj
        
        # 범위 안에 있고, 아직 방문하지 않은 곳이라면
        if 1<=ni<=N and 1<=nj<=M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            cnt += arr[ni][nj]
            dfs(ni,nj)
            cnt -= arr[ni][nj]
            visited[ni][nj] = 0



N, M = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
visited = [[0]*(M+1) for _ in range(N+1)]

max_val = 0
cnt = 0

for val in arr:
    print(val)
for val in visited:
    print(val)

dfs(1,1)

print(max_val)


