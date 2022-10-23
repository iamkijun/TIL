import sys
sys.stdin = open('Data_Structure/input.txt')

from collections import deque

N,M = map(int,input().split())

board = [0] * 101

def bfs(ci):
    q = deque()
    q.append([ci,0])
    visited = [0] * 101
    visited[1] = 1

    while q:
        # print(q)
        ci, cnt = q.popleft()

        if ci == 100:
            return cnt

        for i in range(1,7):
            ni = ci + i
            if 1<=ni<=100:
                if ladder[ni]:
                    visited[ni] = 1
                    visited[ladder[ni][0]] = 1
                    q.append([ladder[ni][0],cnt+1])
                elif snake[ni]:
                    visited[ni] = 1
                    visited[snake[ni][0]] = 1
                    q.append([snake[ni][0],cnt+1])
                elif not visited[ni]:
                    visited[ni] = 1
                    q.append([ni,cnt+1])

ladder = [[] for _ in range(102)]
for n in range(N):
    x, y = map(int, input().split())
    ladder[x].append(y)

snake = [[] for _ in range(102)]
for m in range(M):
    u, v = map(int, input().split())
    snake[u].append(v)

print(bfs(1))



