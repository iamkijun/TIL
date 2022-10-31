from calendar import c
import sys
sys.stdin = open('IM추천문제/input.txt','r')

for t in range(1,2):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # [1] 전치행렬로 전환
    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    cnt = 0         #교착 상태의 개수

    # [2] 1행씩 stk작업
    for i in range(100):
        stk = []
        for j in range(100):
            if arr[i][j] == 1:
                stk.append(1)

            elif arr[i][j] == 2:
                stk.append(2)

            elif arr[i][j] == 0:
                if len(stk) >=2:
                    print(stk)
                    stk.clear()
    
    print(f'#{t} {cnt}')
    