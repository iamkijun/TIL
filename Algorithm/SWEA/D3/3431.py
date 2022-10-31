import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):

    L, U, X = map(int, input().split())

    if L < X and X < U:
        print(f'#{t} 0')
    elif X < L:
        print(f'#{t} {L-X}')
    elif U < X:
        print(f'#{t} -1')