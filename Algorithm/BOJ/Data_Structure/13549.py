import sys
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque   

N, K = map(int, input().split())

visited = [0]  * 100001

q = deque()
q.append(N)
visited[N] = 1

while q:    
    current = q.popleft()

    if current == K:
        print(visited[current]-1)
        break
    
    for n in (current*2,current+1,current-1):
        if 0 <= n <= 100000 and not visited[n]:
            if n == current*2:
                visited[n] = visited[current]
                q.appendleft(n)
            else:
                visited[n] = visited[current] + 1
                q.append(n)