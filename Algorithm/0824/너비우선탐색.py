import sys
sys.stdin = open('0824/input.txt','r')

def bfs(arr, start):
    que = [start]

    visited[start] = 1

    while que:
        node = que.pop(0)
        if not visited[node]:
            visited[node] = 1
            que.append(node)
            print(node, end=' ')

        for li in arr:
            if li[0] == node and not visited[li[node]]:
                que.append()

# T = 10
T = int(input())
for test_case in range(1, T + 1):

    V, E = map(int,input().split())

    arr = [list(map(int, input().split())) for _ in range(E)]

    visited = [0] * (V+1)

    print(f'#{test_case}', end=' ')
    bfs(arr, 1)
    print()

