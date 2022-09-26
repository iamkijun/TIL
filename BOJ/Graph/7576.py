import sys
sys.stdin = open("Graph/input.txt","r")

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

di =[-1,1,0,0]
dj =[0,0,-1,1]

for val in arr:
    print(val)