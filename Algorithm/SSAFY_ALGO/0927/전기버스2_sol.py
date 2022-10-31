import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n, cnt, sm):
    global ans
    if ans <=  cnt:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    if sm>0:                   #교체하지 않는 경우
        dfs(n+1,cnt,sm-1)
    dfs(n+1, cnt+1,li[n]-1)

for t in range(1,T+1):
    li = list(map(int, input().split()))

    N = li[0]
    ans = N             #최소값의 초기값 설정

    dfs(2, 0, li[1]-1)      #index 번호, count횟수, 기름량

    print(f'#{t} {ans}')