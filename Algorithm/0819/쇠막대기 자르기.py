import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):
    li = list(map(str,input()))
    count = 0

    count_left = 0  # (의 개수
    count_right = 0 # )의 개수

    arr = [] # 큰 리스트 선언
    idx = 0 # 완전 끝나는 인덱스 값 저장

    for i in range(len(li)): # 청크 단위로 나누기
        if li[i] == '(':
            count_left += 1
        elif li[i] == ')':
            count_right += 1

        if count_left == count_right:
            arr.append(li[idx:i+1])
            idx=i+1

    total = 0 # 생기는 총 꼬다리 변수로 선언

    for i in range(len(arr)):

        count = 0 # 꼬다리의 개수 변수로 선언

        if len(arr[i]) == 2:
            continue # () 일경우에는 없으니까 패스

        for j in range(len(arr[i])):
            if arr[i][j] == '(':
                count += 1 # 문 열리면서 생기는 잠재적 꼬다리 하나 만들기

            elif arr[i][j] == ')':
                count -= 1 # 문 닫아주면서 생기는 잠재적 꼬다리 하나 없애기

                if arr[i][j-1] == '(':
                    total += count # 레이저 쏘는 위치에서 나오는 왼쪽 꼬다리

                else:
                    total += 1 # 맨 오른쪽 꼬다리

    print(f'#{t} {total}')