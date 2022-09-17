import sys
sys.stdin = open('DP/input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input())

    cnt = 1

    if N == M:
        print(cnt)
    else:
        for i in range(M-N):
            