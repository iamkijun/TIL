import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n, sm):
    global ans

    if sm > ans:
        return

    if n > 12:
        ans = min(ans,sm)
        return

    #일일권
    dfs(n+1,sm+plan[n]*day)
    #한달권
    dfs(n+1,sm+mon)
    #분기권
    dfs(n + 3, sm + mon3)
    #년권
    dfs(n + 12, sm + year)

for t in range(1,T+1):

    day, mon, mon3, year = map(int,input().split()) #1일, 1개월, 3개월, 1년
    plan = [0] + list(map(int,input().split())) #1월 ~ 12월
    ans = 3000
    dfs(1,0)

    print(f'#{t} {ans}')