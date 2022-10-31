import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n,sm):
    global ans

    if n==N:
        if sm>=B and ans>sm-B:
            ans = sm-B
        return

    dfs(n+1, sm+li[n])
    dfs(n+1, sm)

for t in range(1,T+1):

    N, B = map(int, input().split())

    li = list(map(int, input().split()))

    ans = 10000*N
    dfs(0,0)

    print(f'#{t} {ans}')