import sys
sys.stdin = open("0819/input.txt","r")

import copy

for t in range(1,11):

    N = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] #양 열 끝에 0 추가

    is_one = []  # 시작점에 1이 있는 인덱스 리스트

    for i in range(1,101):
        if arr[0][i] == 1:
            is_one.append(i)

    min_idx = 0 #최소값을 가지는 인덱스
    min_count = 10000

    for j in range(len(is_one)):
        i = 0
        arr1 = copy.deepcopy(arr)        # 해당 is_one[j]에서 쓸 array 딥카피로 불러옥;
        val = is_one[j]                  # val 선언
        count = 0                        #개수 세기
        while i < 100:

            if arr1[i][val-1] == 1:      #왼쪽에 1이 있을 경우
                arr1[i][val] = 0         #지나온 길을 0으로 만들고
                val = val-1              #왼쪽 열로 이동
            
            elif arr1[i][val+1] == 1:    #오른쪽에 1이 있을 경우
                arr1[i][val] = 0         #지나온 길을 0으로 만들고
                val = val +1             #오른쪽 열로 이동
            
            else:
                i += 1                   #아래로 이동

            count +=1
        
        if count < min_count:            #최소값 찾기
            min_idx = is_one[j]
            min_count = count

    print(f'#{N} {min_idx-1}')


