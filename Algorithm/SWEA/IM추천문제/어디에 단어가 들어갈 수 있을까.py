import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())

    #상하좌우 0으로 둘러싸기
    arr = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
    
    #글자를 넣을 수 있다는 의미를 가지는 리스트
    one_list = [1] * K
    
    count = 0

    # [1] 행에 글자를 넣을 수 있는 경우 찾기
    for i in range(1,N+1):
        for j in range(1,N-K+2):
            # 해당 범위기 전부 1이고, 왼쪽 오른쪽이 0이라 딱 들어맞는 경우 찾기
            if arr[i][j:j+K] == one_list and arr[i][j-1] == 0 and arr[i][j+K] == 0:
                count +=1
    
    # [2] 전치행렬로 바꾸기
    for i in range(N+2):
        for j in range(N+2):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # [3] 행으로 전환한 열에 있는 글자를 넣을 수 있는 경우 찾기
    for i in range(1,N+1):
        for j in range(1,N-K+2):
            # 해당 범위기 전부 1이고, 왼쪽 오른쪽이 0이라 딱 들어맞는 경우 찾기
            if arr[i][j:j+K] == one_list and arr[i][j-1] == 0 and arr[i][j+K] == 0:
                count +=1

    print(f'#{t} {count}')