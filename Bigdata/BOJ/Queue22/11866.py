import sys
sys.stdin = open('Queue22/input.txt','r')

from collections import deque

N, K = map(int, input().split())

queue = [x for x in range(1,N+1)]

ans = []

first = K-1
while True:
    ans.append(str(queue.pop(first%len(queue))))
    if not queue:
        break
    else:
        first = (first + K-1) % (len(queue))

print("<",end='')
print(', '.join(ans),end='')
print(">")
