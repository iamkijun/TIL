import sys
sys.stdin = open('IM추천문제/input.txt','r')

for _ in range(10):
    T = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    s_list = [] #시작점의 인덱스들이 담겨있는 리스트

    for i in range(1,101):
        if arr[0][i] == 1:
            s_list.append(i)

    cnts = [] # 개수를 담아놓는 리스트

    for k in range(len(s_list)):
        val = s_list[k]     #열을 담을 변수 선언(초기값: 시작점)
        j= 0                #0행부터 시작
        cnt = 0             #움직인 횟수 세기

        while j != 99: #맨 끝 행에 도착할 때 까지 반복
            if arr[j][val+1] == 1:              #우측열로 이동
                while True:
                    val += 1
                    cnt += 1
                    if arr[j][val+1] == 0:      #막다른길에 위로
                        j += 1
                        cnt += 1
                        break
            
            elif arr[j][val-1] == 1:            #좌측열로 이동
                while True:
                    val -= 1
                    cnt += 1
                    if arr[j][val-1] == 0:      #막다른길에 위로
                        j += 1
                        cnt += 1
                        break

            else:
                j += 1                          #좌우 길이 없을 때 위로
                cnt += 1

        cnts.append(cnt)
        
    min_cnt = cnts[0]
    min_idx = 1

    for k in range(len(s_list)):
        if cnts[k] < min_cnt:
            min_cnt = cnts[k]
            min_idx = s_list[k]
    
    print(f'#{T} {min_idx-1}')