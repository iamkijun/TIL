import sys
sys.stdin = open('Queue/input.txt','r')

from collections import deque

N = int(input())

queue = list(map(int, input().split()))
idx = [x for x in range(1,N+1)]

ans = []
cnt = 0


while len(ans)<N-1:
    a = queue[0]
    b = idx[0]

    if a < 0:
        
        ans.append(idx.pop(0))
        queue.pop(0)

        for i in range(a*(-1)):
            idx.insert(0,idx.pop())
            queue.insert(0,queue.pop())
        
    elif a > 0:
        ans.append(idx.pop(0))
        queue.pop(0)
        
        for i in range(a-1):
            idx.append(idx.pop(0))
            queue.append(queue.pop(0))

ans.append(idx[0])
print(*ans)