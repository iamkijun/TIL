import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T + 1):

    N, K_min, K_max = map(int, input().split())

    N_list = list(map(int, input().split()))
    set_N = set(N_list)
    set_li_N = list(set_N)
    print(set_li_N)
    N_list.sort()

    diff_list = []
    for i in range(len(set_li_N) - 1):
        for j in range(i, len(set_li_N)):

            T1, T2 = set_li_N[i+1], set_li_N[j]

            if T1 >= T2:
                continue
            print(T1,T2)
            A, B, C = [], [], []

            A = N_list[:N_list.index(T1)]
            B = N_list[N_list.index(T1):N_list.index(T2)]
            C = N_list[N_list.index(T2):]

            if K_min <= len(A) <= K_max and K_min <= len(B) <= K_max and K_min <= len(C) <= K_max:
                diff = max([len(A), len(B), len(C)]) - min([len(A), len(B), len(C)])
                diff_list.append(diff)
            else:
                pass

    if diff_list:
        print(f'#{t} {min(diff_list)}')
    else:
        print(f'#{t} {-1}')