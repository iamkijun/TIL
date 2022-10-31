import sys
sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1):

    N, M, K = map(int, input().split())

    N_list = list(map(int, input().split()))

    #손님들은 순서대로 오니까 오름차순으로 정렬 (버블소트)
    for i in range(N-1,0,-1):
        for j in range(i):
            if N_list[j] > N_list[j+1]:
                N_list[j], N_list[j+1] = N_list[j+1], N_list[j]

    now_bread = 0   #현재 빵의 초기값 ( 아직 만든게 없으니까)
    sold_bread = 0  #판 빵의 초기값 ( 아직 판게 없으니까)
    for i in range(N):
        s = N_list[i]           #현재시간(초)
        made_bread = s//M *K    #만든 붕어빵의 갯수 : (걸린시간 // 만드는데 걸리는 시간) * 한번에 만들 수 있는 개수
        now_bread = made_bread - sold_bread     #현재 붕어빵의 개수 : 만든거 - 판거

        if now_bread >= 1:      #지금 빵이 하나 이상 있을 때 (판매 가능할 때)
            sold_bread +=1      #판매된 빵의 갯수 추가
        else:                   #지금 빵이 없을 때 ( 판매 불가능할 때)
            print(f'#{t} Impossible')
            break
    else:
        print(f'#{t} Possible')


