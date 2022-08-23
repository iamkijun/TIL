import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]

    si = 0
    sj = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
                break

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    while True:
        for i in range(4):
            if arr[si+di[i]][sj+dj[i]] == 0:

    print(si,sj)