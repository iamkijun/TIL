import sys

sys.stdin = open('Data_Structure/input.txt','r')
# input = sys.stdin.readline

from heapq import heappush,heappop

N = int(input().strip())

arr = []

for i in range(N):
    x = int(input().strip())

    if x == 0:
        if arr:
            print(heappop(arr)[1])
        else:
            print(0)
    else:
        heappush(arr,[abs(x),x])

    # print(arr)