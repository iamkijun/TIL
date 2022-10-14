import sys
sys.stdin = open('Queue22/input.txt','r')

from collections import deque

N, M = map(int, input().split())

queue = deque([x for x in range(1,N+1)])

li = list(map(int, input().split()))

cnt = 0

for i in range(M):
    if li[i] == queue[0]:
        queue.popleft()
    else:
        if queue.index(li[i]) < len(queue)-queue.index(li[i]):
            while True:
                
                if li[i] == queue[0]:
                    del queue[0]
                    break
                else:
                    queue.append(queue[0])
                    del queue[0]
                    cnt+=1
        
        else:
            while True:
                
                if li[i] == queue[0]:
                    del queue[0]
                    break
                else:
                    queue.insert(0,queue[-1])
                    del queue[-1]
                    cnt+=1

print(cnt)
