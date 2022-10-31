import sys
sys.stdin = open('input.txt','r')

def post(n):
    if li[n]:       #노드가 존재하는 경우
        if li[n] == '+':
            return post(ch1[n]) + post(ch2[n])
        elif li[n] == '-':
            return post(ch1[n]) - post(ch2[n])
        elif li[n] == '*':
            return post(ch1[n]) * post(ch2[n])
        elif li[n] == '/':
            return post(ch1[n]) / post(ch2[n])
        else:
            return int(li[n])

for t in range(1,11):

    N = int(input())
    li = [0] * (N+1)

    ch1 = [0] * (N+1)
    ch2 = [0] * (N + 1)

    #[1] 트리 구조에 맞게 저장
    for _ in range(N):
        new = input().split()
        p = int(new[0])
        li[p] = new[1]
        if len(new) > 2:
            ch1[p] = int(new[2])
            ch2[p] = int(new[3])

    #[2] post order순회하면서 계산
    ans = post(1)

    print(f'#{t} {int(ans)}')