
import queue
import sys
sys.stdin = open('Sort/input.txt','r')

from collections import deque

N = int(input())
li =[] 
for n in range(N):
    li.append(int(input()))

li = deque(reversed(li))

ans = 0
while len(li) >=2:
    temp = li[-1]+li[-2]
    ans+=temp
    
    li.pop()
    li.pop()

    li.append(temp)

    li = deque(reversed(li))

print(ans)