import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T+1):

    N, K = map(int,input().split())

    li = [N//K] * K # 모두 같은 값으로 초기화

    #나머지를 li[0]~ 하나씩 추가
    ans =1

    for i in range(N%K):
        li[i] += 1

    for val in li:
        ans *= val

    print(f'#{t} {ans}')
