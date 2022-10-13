import sys
sys.stdin = open('SAMSUNG/input.txt','r')

from collections import deque

N = int(input())

def bfs():
    global cnt

    q = deque()
    q.append([[1,1],[1,2]])

    while q:
        pipe = q.popleft()

        if pipe[1][0] == N and pipe[1][1] == N:
            cnt += 1
            return

        # [1] 가로일 경우
        if pipe[0][0] == pipe[1][0] and pipe[0][1] + 1 == pipe[1][1]:
            # [1-1] 가로 추가
            if pipe[1][1] +1 <= N and arr[pipe[1][0]][pipe[1][1] + 1] != 0:
                q.append([[pipe[1][0], pipe[1][1]],[pipe[1][0], pipe[1][1] + 1]])
            # [1-2] 대각선 추가
            if pipe[1][0] +1 <=N and pipe[1][1] +1 <= N and arr[pipe[1][0] + 1][pipe[1][1] + 1] != 0:
                q.append([[pipe[1][0], pipe[1][1]],[pipe[1][0]+1, pipe[1][1] + 1]])
            
        # [2] 세로일 경우
        elif pipe[0][0]+1 == pipe[1][0] and pipe[0][1] == pipe[1][1]:
            # [2-1] 세로 추가
            if pipe[1][0] +1 <= N:
                q.append([[pipe[1][0], pipe[1][1]],[pipe[1][0], pipe[1][1] + 1]])

        # [3] 대각선일 경우


    
    return



arr = [[1] * (N+1)] + [[1] + list(map(int, input().split())) for _ in range(N)]

for val in arr:
    print(val)
