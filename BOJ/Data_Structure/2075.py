import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt','r')

import heapq

N = int(input())

arr = []

for i in range(N):
    li = list(map(int, input().split()))
    if arr:
        for val in li:
            heapq.heappush(arr,val)
            heapq.heappop(arr)
    else:
        arr = li

print(arr[0])
