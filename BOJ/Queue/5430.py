import sys
sys.stdin = open('Queue/input.txt','r')

from collections import deque

import itertools

T = int(input())

for t in range(T):

    equ = input()

    N = int(input())

    queue = input()[1:-1].split(',')
    queue= deque(queue)

    if N ==0:
        queue = []
    flip = 0
    
    for val in equ:
        if val == 'R':
            flip +=1
        elif val == 'D':
            if len(queue) < 1:
                print('error')
                break

            if flip % 2 == 0:
                queue.popleft()
            else:
                queue.pop()
    else:
        if flip % 2 == 1:
            queue.reverse()
        
        print("["+",".join(queue)+"]")

