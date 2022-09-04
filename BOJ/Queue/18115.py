import sys
sys.stdin = open('Queue/input.txt','r')

from collections import deque

N = int(input())

li = list(map(int, input().split()))

idx = [x for x in range(N,0,-1)]


ans =[]
for i in range(1,1+N):
    print(idx)
    if li[i-1] == 1:
        ans.append(idx.pop(0))
    elif li[i-1] == 2:
        ans.append(idx.pop(1))
    elif li[i-1] == 3:
        ans.append(idx.pop(-1))

print(*ans)