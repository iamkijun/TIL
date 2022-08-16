import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):

    N = int(input())

    li = list(map(int, input().split()))

    total = 0

    while True:
        # 모든 검색 마쳤을 때 종료
        if len(li) <= 1:
            break

        ''' 
        메소드를 사용 안하고 싶었지만, 런타임 에러가 나서 사용 못했습니다(너무 느림)
        maxV = li[0]
        idx = 0

        for i in range(len(li)):
            if li[i] > maxV:
                maxV = li[i] 
                idx = i      # 인덱스 값 저장
        '''

        # 최댓값 찾는 메소드 활용
        maxV = max(li)
        idx = li.index(maxV) # 인덱스값 저장


        zero_list= [0] * len(li) # 0으로 가득찬 리스트 생성
        zero_list= [maxV] * idx # 최댓값으로 가득찬 리스트로 변환

        total += sum(zero_list[:idx]) - sum(li[:idx]) # 최댓값으로 가득찬 리스트 합 - 원래 리스트 합

        li = li[idx+1:] #기존 리스트를, 더한걸 없앤 값으로 바꾸기

    print(f'#{t} {total}')




