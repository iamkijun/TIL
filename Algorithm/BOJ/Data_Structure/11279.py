import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt','r')

from heapq import heappush,heappop

N = int(input().strip())

arr = []

for _ in range(N):
    x = int(input().strip())

    if x == 0:
        if arr:
            print(-heappop(arr))
        else:
            print(0)
    else:
        heappush(arr,-x)
        


