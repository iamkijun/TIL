import sys

sys.stdin = open('Data_Structure/input.txt')

from collections import deque

def bfs(current):
    q = deque()
    q.append(current)
    
    cnt= 0
    while q:
        
        current = q.popleft()

        if current == K:
            return visited[current]
        
        for n in (current+1,current-1,current*2):
            if 0 <= n <= 100000 and not visited[n]:
                q.append(n)
                visited[n] = visited[current] + 1
    


N, K = map(int, input().split())

visited = [0]  * 100001

ans = bfs(N)

print(ans)