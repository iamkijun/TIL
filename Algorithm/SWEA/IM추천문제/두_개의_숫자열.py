import sys
sys.stdin = open('input.txt','r')

T= int(input())

for t in range(1,T+1):

    N, M= map(int,input().split())

    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    total_list = []

    # [1-1] M이 N보다 클 때,
    if M > N:
        for i in range(M-N+1):
            total = 0  
            
            for j in range(N):
                total += N_list[j]*M_list[j+i]

            total_list.append(total)
    
    # [1-2] N이 M보다 클 때,
    elif N > M:
        for i in range(N-M+1):
            total = 0
            
            for j in range(M):
                total += N_list[j+i]*M_list[j]

            total_list.append(total)
    
    # [1-3] N == M:
    else:
        total = 0
        for i in range(N):
            total += N_list[i]*M_list[i]

    # [2] 최대값 찾기
    if total_list:
        # 선택정렬 활용
        for i in range(len(total_list)-1):
            max_idx = i
            for j in range(i,len(total_list)):
                if total_list[j] > total_list[max_idx]:
                    max_idx = j
            total_list[max_idx], total_list[i] = total_list[i], total_list[max_idx]

        total = total_list[0]
    
    print(f'#{t} {total}')
