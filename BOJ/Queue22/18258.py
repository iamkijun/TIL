import sys
sys.stdin = open('input.txt','r')

from collections import deque
N = int(input())

queue = deque()
for _ in range(N):

    x=  list(map(str, input().split()))

    if x[0] == 'push':
        queue.append(int(x[1]))
    elif x[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif x[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)