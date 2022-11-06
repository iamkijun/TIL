cost = [19,78,27,18,20]
x = 25

def solution(cost, x):
    
    #최대값 변수 초기선언
    max_num = 0
    #최대값 인덱스 변수 초기선언
    max_idx = 0

    #최대값 인덱스 찾기
    for i in range(len(cost)-1,0,-1):
        if cost[i] <= x:
            max_idx = i
            max_num += 2**i
            break
    else:
        #예외처리 (얻을 수 있는 물감이 하나도 없을 경우)
        return 0
    
    #현재 남은 금액 변수 선언
    left = x - cost[max_idx]

    #탑다운으로 탐색해나갈 인덱스 변수 선언
    idx = max_idx

    #인덱스 번호가 높은 물감을 현재 남은돈으로 살 수 있는지 확인
    while left > 0 and idx > 0:
        idx -= 1
        if left >= cost[idx]:
            left -= cost[idx]
            max_num += 2**idx

    return max_num % (10**9 + 7)

print(solution(cost,x))