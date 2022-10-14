import sys
sys.stdin = open('input.txt','r')

from collections import deque
N = int(input())

queue = deque()

for _ in range(N):
    x = list(map(str,input().split()))

    if x[0] == 'push_front':
        queue.appendleft(x[1])
    elif x[0] == 'push_back':
        queue.append(x[1])
    elif x[0] == 'pop_front':
        if len(queue) >= 1:
            print(queue.popleft())
        else:
            print(-1)
    elif x[0] == 'pop_back':
        if len(queue) >= 1:
            print(queue.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if len(queue) >= 1:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
