import sys
sys.stdin = open("Graph/input.txt","r")

'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cheeze = 0

for i in range(1,N):
    for j in range(1,M):
        
        if arr[i][j] == 1:
            print(i,j)
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i+di, j+dj
                if arr[ni][nj] == 0:
                    break
            else:
                arr[i][j] = 2
cnt= 1
while cnt>0:
    cnt = 0
    for i in range(1,N):
        for j in range(1,M):
            if arr[i][j]>=1:
                cnt+=1
                arr[i][j] -=1

    print(cnt)

for val in arr:
    print(val)