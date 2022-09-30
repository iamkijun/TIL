import sys
sys.stdin = open('input.txt','r')
'''
0100
1110
1011
1010
'''
T = int(input())

def bfs(n):
    for i in range(1,n):
        j = n-i
        if 1<= i <N and 1<= j <N:

            arr[i][j] += min(arr[i-1][j],arr[i][j-1])

for t in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = int(arr[i][j])

    for a in range(2,2*N):
        bfs(a)

    print(f'#{t} {arr[N-1][N-1]}')

