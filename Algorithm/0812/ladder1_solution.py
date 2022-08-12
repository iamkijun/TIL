import sys
sys.stdin = open("input.txt", "r")

for t in range(1,4):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 초기값 설정
    i, j = 99, 0
    for tj in range(100):
        if arr[i][tj] == 2:
            j = tj
            break

    while i>0:
        #왼쪽 먼저 체크
        if j >0 and arr[i][j-1] == 1:
            arr[i][j] = 0
            j -=1
        #오른쪽 체크
        elif j <99 and arr[i][j+1] == 1:
            arr[i][j] =0
            j +=1
        else:
            i-=1


    print(f'#{t} {j}')