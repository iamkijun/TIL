import sys
sys.stdin = open('input.txt','r')

def dfs(n, sm): #시작, 합계
    global ans

    #가지치기는 제일 위에서, 제일 마지막 순서로
    if sm > K or s:
        return

    # 종료조건
    if n==N:
        if sm == K:
            ans += 1
        return

    # n+1 호출
    # 사용하는 경우
    dfs(n+1, sm+li[n])
    # 사용하지 않는 경우
    dfs(n+1, sm)

T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())

    li = list(map(int, input().split()))

    ans = 0

    dfs(0, 0) #시작, 합계

    print(f'#{t} {ans}')