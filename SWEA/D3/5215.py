import sys
sys.stdin = open("D3/input.txt")

TC = int(input())

for t in range(1,TC+1):

    N, L = map(int, input().split())

    T_list = []
    K_list = []

    for _ in range(N):
        T, K = map(int, input().split())
        T_list.append(T)
        K_list.append(K)

    max_T = 0

    for i in range(1<<N):
        sum_T = 0
        sum_K = 0
        for j in range(N):
            if i % (1<<j):
                sum_T += T_list[j]
                sum_K += K_list[j]
                print(T_list[j],K_list[j], end=", ")
        print(sum_T,sum_K)
        if sum_T > max_T and sum_K < L:
            sum_T = max_T

    print(f'#{t} {max_T}')