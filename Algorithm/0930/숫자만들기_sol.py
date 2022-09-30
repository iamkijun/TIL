import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(n, num, n1,n2,n3,n4):
    global max_val, min_val

    if n==N:
        min_val = min(min_val,num)
        max_val = max(max_val,num)
        return

    if n1:
        dfs(n+1, num+num_li[n], n1-1, n2, n3, n4)
    if n2:
        dfs(n+1, num-num_li[n], n1, n2-1, n3, n4)
    if n3:
        dfs(n+1, num*num_li[n], n1, n2, n3-1, n4)
    if n4:
        dfs(n+1, int(num/num_li[n]), n1, n2, n3, n4-1)


for t in range(1,T+1):
    N = int(input())

    add, sub, mul, div = map(int,input().split())
    num_li = list(map(int, input().split()))

    max_val = int(-1e8)
    min_val = int(1e8)

    dfs(1,num_li[0],add,sub,mul,div)

    print(f'#{t} {max_val-min_val}')