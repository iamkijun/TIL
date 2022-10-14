import sys
sys.stdin = open('Queue22/input.txt','r')

from collections import deque

N = int(input())

li = deque(list(map(int, input().split())))

behind = deque([x for x in range(1,N+1)])
front = deque([])

while li:
    i = li.pop()
    if i == 1:
        front.appendleft(behind.popleft())        
    elif i == 2:
        front.insert(1,behind.popleft())
    elif i == 3:
        front.append(behind.popleft())
        

print(*front)