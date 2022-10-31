import sys
sys.stdin = open('input.txt','r')

T = int(input())

def inorder(n):
    global cnt

    if n <= N:
        inorder(n*2)
        ans[n] = cnt
        cnt +=1
        inorder(n*2+1)

for t in range(1,T+1):

    N = int(input())

    ans = [0] * (N+1)
    cnt = 1
    inorder(1)

    print(f'#{t} {ans[1]} {ans[N//2]}')