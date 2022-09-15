import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,2):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    K = 1
    for i in range(N):

        for j in range(M):
            arr[i][j-k+1:j+k]
