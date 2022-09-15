import sys
sys.stdin = open('input.txt','r')

def postorder(n):
    if n <= N:
        if li[n] == 0:      #하위노드 계산이 필요한 경우
            return postorder(n*2) + postorder(n*2 + 1)
        else:
            return li[n]
    return 0


T = int(input())

for t in range(1,T+1):
    N, M, L = map(int, input().split())
    li = [0]*(N+1)
    for _ in range(M):
        n, v = map(int, input().split()) #노드 n에 v라는 값 저장
        li[n] = v

    ans = postorder(L)

    print(f'#{t} {ans}')
