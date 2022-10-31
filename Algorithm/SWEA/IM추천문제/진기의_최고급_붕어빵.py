import sys
sys.stdin = open('input.txt','r')

T= int(input())

for t in range(1,T+1):

    N, M, K = map(int, input().split())

    N_list = list(map(int, input().split()))

    #빵은 손님들이 오는 순서대로 팔린다.
    #오는 손님들 순서대로 빵을 팔아야 하기 때문에 오름차순 정렬
    #Selection Sort를 활용
    for i in range(N-1):
        min_idx = i
        for j in range(i,N):
            if N_list[j] < N_list[min_idx]:
                min_idx = j
        N_list[i], N_list[min_idx] = N_list[min_idx], N_list[i]

    
    sold_bread = 0 #팔린 빵 숫자
    
    iserror = 0 #에러가 있는지 판단하기 위해 선언

    for i in range(N):
        s = N_list[i] #해당 시간에
        
        make_bread = s // M * K #만들어진 빵의 총 갯수

        now_bread = make_bread - sold_bread #보유중의 빵 갯수 = 만든 빵 - 팔린 빵

        if now_bread >=1:       #팔 수 있는 빵이 존재한다면
            sold_bread += 1     #판매 빵 갯수 1 증가
            pass
        else:                   #팔 수 있는 빵이 존재하지 않다면
            iserror = 1         #에러 발생, 탈출
            break
    
    if iserror:
        print(f'#{t} Impossible')
    else:
        print(f'#{t} Possible')