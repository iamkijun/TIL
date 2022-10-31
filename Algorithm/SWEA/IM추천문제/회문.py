import sys
sys.stdin = open('IM추천문제/input.txt','r')

for t in range(1,11):
    N = int(input())

    arr = [list(map(str, input())) for _ in range(8)]

    cnt= 0
    # [1] 행에 있는 가로 회문 찾기
    for i in range(8):
        for j in range(9-N):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1
    
    # [2] 전치행렬을 이용하여 세로를 가로로 전환
    for i in range(8):
        for j in range(8):
            if i < j :
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # [3] 행에 있는 세로 회문 찾기
    for i in range(8):
        for j in range(9-N):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1
    
    print(f'#{t} {cnt}')