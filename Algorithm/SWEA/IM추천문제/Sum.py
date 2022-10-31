import sys
sys.stdin = open('IM추천문제/input.txt','r')

for _ in range(10):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    max_r = 0   #행의 총합 가운데 최대값 저장
    max_c = 0   #열의 총합 가운데 최대값 저장
    
    sum_cross1 = 0      #대각선 (\)저장
    sum_cross2 = 0      #대각선 (/)저장

    for i in range(100):
        sum_r = 0   #행의 총합 담아두는 변수
        sum_c = 0   #열의 총합 담아두는 변수

        for j in range(100):
            sum_r += arr[i][j]
            sum_c += arr[j][i]
        
        if sum_r > max_r:
            max_r = sum_r
        
        if sum_c > max_c:
            max_c = sum_c

        sum_cross1 += arr[i][i]             #대각선 (\)저장
        sum_cross2 += arr[99-i][i]          #대각선 (/)저장
    
    #최대값 maxV로 선언
    if max_r >= max_c:
        maxV = max_r
    elif max_c > max_r:
        maxV = max_c
    
    #maxV와 대각선 최대값 비교
    if sum_cross1 > maxV:
        maxV = sum_cross1
    if sum_cross2 > maxV:
        maxV = sum_cross2


    print(f'#{T} {maxV}')