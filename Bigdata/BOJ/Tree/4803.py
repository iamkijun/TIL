import sys
# input = sys.stdin.readline
sys.stdin = open('Tree/input.txt','r')

def dfs(pre, v):
    # 방문처리
    visited[v] = True

    for node in graph[v]:
        # 자식노드가 부모노드와 같으면 수행X
        if node == pre:
            continue
        # 이미 방문한 경우, 연결돼 있다는 뜻
        if visited[node]:
            return False
        # 연결되어 있을 경우
        if not dfs(v, node):
            return False
        
    return True

t = 0
while True:
    t += 1

    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):

        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0

    for i in range(1,n+1):
        if not visited[i]:
            if dfs(0, i):
                cnt += 1

    if cnt == 0:
        print(f'Case {t}: No trees.')
    elif cnt == 1:
        print(f'Case {t}: There is one tree')
    else:
        print(f'Case {t}: A forest of {cnt} trees.')