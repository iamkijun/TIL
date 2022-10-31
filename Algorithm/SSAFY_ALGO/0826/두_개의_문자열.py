import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))

    M_list = list(map(int, input().split()))
    
    # [1-1] N>M:
    if N> M:
        max_total = 0 #최대값 저장할 변수 선언
        # max_total의 초기값 설정
        for m in range(M):
            max_total += N_list[m] * M_list[m]            
        
        # 최대값 찾기
        for k in range(N-M+1):          # N에서 이동할 길이
            total = 0
            for i in range(M):          # M의 길이가 짧으니 M의 길이만큼은 다 돌아아됨
                total += N_list[i+k]*M_list[i]
            if total > max_total:
                max_total = total

    # [1-2] M>N:
    elif M> N:
        max_total = 0  # 최대값 저장할 변수 선언
        # max_total의 초기값 설정
        for n in range(N):
            max_total += N_list[n] * M_list[n]

        for k in range(M-N+1):          # M에서 이동할 길이
            total = 0
            for i in range(N):          # N의 길이가 짧으니 M의 길이만큼은 다 돌아아됨
                total += N_list[i]*M_list[i+k]
            if total > max_total:
                max_total = total
    # [1-3] N == M: (최초 total = max_total이 된다.)
    else:
        max_total = 0  # 최대값 저장할 변수 선언
        for i in range(N):
            max_total += N_list[i]*M_list[i]

    print(f'#{t} {max_total}')
