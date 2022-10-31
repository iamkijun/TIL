import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):

    N, Q = map(int, input().split())

    li = [0] * N

    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(R-L+1):
            li[L-1+j] = i

    print(f'#{t}', *li)