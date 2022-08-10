import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1):
    N, Q = map(int, input().split())

    box = [0] * 5

    for j in range(Q):
        L, R = map(int, input().split())
        for k in range(R-L+1):
            box[j+k] = j+1

    print(f'#{i}',*box)