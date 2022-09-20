for num in range(1,11):
    n = int(input()) # Test Case 외치기

    li =[] # 새 리스트 선언

    for _ in range(100): #리스트 li에 100개의 리스트 추가
        a= list(map(int, input().split()))
        li.append(a)

    total = 0 # 찾아나가야 할 최종 값
    totalvs = 0 # 열의 총합을 넣을 변수 선언
    x1 = 0 #대각선 1번 총합 
    x2 = 0 #대각선 2번 총합

    for i in range(100):
        if sum(li[i]) > total: #행의 총합을 현재까지의 max 값과 비교
            total = sum(li[i])
        for j in range(100): # 열의 총합을 현재까지의 max 값과 비교
            totalvs += li[j][i]
        if totalvs > total:
            total = totalvs
            totalvs = 0
        else:
            totalvs = 0

        x1 += li[i][i] #대각선 1번 총합 쌓아가는 중
        x2 += li[99-i][i] #대각선 2번 총합 쌓아가는 중

    if x1 > total: #대각선 1번과 최대값 비교
        total = x1 
    if x2 > total: #대각선 2번과 최대값 비교
        total = x2
    
    print(f'#{n} {total}')
