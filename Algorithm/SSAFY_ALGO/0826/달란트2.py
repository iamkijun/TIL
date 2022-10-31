import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T+1):

    N, P = map(int,input().split())

    max_candy = 0

    val = N//P
    if val*P == N:
        max_candy = val**P
        print(f'#{t} {max_candy}')
    else:
        diff = N-val*P

        max_candy = val**(P-diff) * (val+1)**diff
        print(f'#{t} {max_candy}')
