import sys
sys.stdin = open("Graph/input.txt","r")

# from collections import deque

W,H = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(H)]

for val in arr:
    print(val)