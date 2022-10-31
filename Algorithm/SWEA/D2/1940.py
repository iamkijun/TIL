T = int(input())

for i in range(1,T+1):
    N = int(input())

    distance = 0
    b_list = [0] 

    for j in range(N):
        a = list(map(int, input().split()))
        if a[0] == 0: # 현재 속도 유지
            distance = distance + b_list[-1]
            
        elif a[0] == 1: # 가속
            distance = distance + (b_list[-1] + a[1])
            b_list.append(b_list[-1] + a[1])
            
        elif a[0] == 2: # 감속
            if a[1] > b_list[-1]:
                a[1] = 0
            distance = distance + (b_list[-1] - a[1])
            b_list.append(b_list[-1] - a[1])
            
    print(f'#{i} {distance}')