import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1):

    N, M = map(int, input().split())

    a = list(map(int, input().split()))

    sm = 0
    for j in range(M):
        sm += a[j]

    mn = mx = sm

    for k in range(M,N):
        sm = sm + a[k] - a[k-M]
        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm

    result = mx-mn

    print(f'#{i} {result}')
    # min_sum = 1000000 * M #가장 작
    # max_sum = 0 #가장 큰
    #
    # for l in range(len(a)-M+1):
    #     max_val = 0
    #     min_val = 0
    #
    #     for k in range(0,M):
    #         max_val += a[l+k]
    #         min_val += a[l+k]
    #
    #     if min_val < min_sum:
    #         min_sum = min_val
    #     if max_val > max_sum:
    #         max_sum = max_val
    #
    # result = max_sum - min_sum
    # print(f'#{i} {result}')