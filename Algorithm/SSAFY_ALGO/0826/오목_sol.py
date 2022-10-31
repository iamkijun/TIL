import sys
sys.stdin = open('input.txt','r')

def omok(N, arr):
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[1,1],[-1,1]]:
                for mul in range(5):
                    ni, nj = i+di*mul, j+dj*mul
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] =='o':
                        pass
                    else:
                        break
                else:
                    return 'YES'

    return 'NO'


T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [str(input()) for _ in range(N)]

    print(f'#{t} {omok(N,arr)}')
