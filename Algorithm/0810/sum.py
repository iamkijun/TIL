import sys
sys.stdin = open("input.txt", "r")

for t in range(1,11):
    N = int(input())
    arr=[]
    for _ in range(100):
        li = list(map(int,input().split()))
        arr.append(li)

    total_h, total_v, total_1, total_2, max_total =0, 0, 0, 0, 0
    #행의 합/열의 합/대각선1의 합/ 대각선 2의 합/ 합이 가장 큰 변수 선언

    for i in range(100):
        for j in range(100):
            total_h += arr[i][j] #행의 합
            total_v += arr[j][i] #열의 합

        if total_h > max_total:
            max_total = total_h

        if total_v > max_total:
            max_total = total_v

        total_h , total_v = 0, 0 # 초기화(i+1에서 다시 쌓아야하니까)

        total_1 += arr[i][i]    #\모양 대각선
        total_2 += arr[99-i][i] #/모양 대각선

    if total_1 > max_total:
        max_total = total_1
    if total_2 > max_total:
        max_total = total_2

    print(f'#{N} {max_total}')


