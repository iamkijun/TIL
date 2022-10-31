import sys
sys.stdin = open('IM추천문제/input.txt','r')

for _ in range(10):
    T = int(input())

    arr = [[0] + list(map(int,input().split())) + [0] for _ in range(100)]

    idx = 0     #도착지점이 있는 열의 index 저장

    for i in range(1,101):
        if arr[99][i] == 2:
            idx = i
            break
    
    j = 99          #밑에서부터 출발

    while j!= 0:

        if arr[j][idx-1] == 1:              #왼쪽으로 이동할 수 있다면
            while True:
                if arr[j][idx-1] == 1:      #왼쪽이 1일때(이동할 수 있을 때)
                    arr[j][idx] = 0         #지나온 곳은 0,
                    idx = idx - 1           #왼쪽으로 한칸 이동
                else:
                    break                   #왼쪽이 0일때, 종료


        elif arr[j][idx+1] == 1:            #오른쪽으로 이동할 수 있다면
            while True:
                if arr[j][idx+1] ==1:       #오른쪽이 1일때(이동할 수 있을 때)
                    arr[j][idx] = 0         #지나온 곳은 0,
                    idx = idx + 1           #오른쪽으로 한칸 이동
                else:
                    break                   #오른쪽이 0일때, 종료

        j -= 1                              #위로 한칸씩 이동
                
    print(f'#{T} {idx-1}')