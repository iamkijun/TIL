import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())

    w_list = list(map(int, input().split()))
    w_list.sort(reverse=True)
    t_list = list(map(int, input().split()))
    t_list.sort(reverse=True)

    ans = 0
    i = 0
    for val in w_list:
        if val <= t_list[i]:
            ans += val
            i += 1
            # 다 돌았을 경우
            if i == M:
                break

    print(f'#{t} {ans}')