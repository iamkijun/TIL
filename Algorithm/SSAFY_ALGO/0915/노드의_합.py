import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M, L = map(int, input().split())

    if N % 2 == 0:
        tree = [0] * (N+2)
    else:
        tree = [0] * (N+1)

    for i in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    while tree[1] == 0:
        for i in range(N,0,-1):
            if tree[i] == 0:
                tree[i] = tree[2*i] + tree[2*i+1]

    print(f'#{t} {tree[L]}')
