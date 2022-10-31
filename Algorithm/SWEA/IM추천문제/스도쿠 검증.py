import sys
sys.stdin = open('input.txt','r')

def sdoku(arr):
    num_set = {1,2,3,4,5,6,7,8,9}

    # [1]  행,열 검사
    for i in range(9):
        h_list = []         #행의 숫자들을 담는 리스트
        v_list = []         #열의 숫자들을 담는 리스트

        for j in range(9):
            h_list.append(arr[i][j]) #행에 있는 값들 저장
            v_list.append(arr[j][i]) #열에 있는 값들 저장

        if set(h_list) != num_set:
            return 0
        elif set(v_list) != num_set:
            return 0

    # [2] 3X3 박스 검사
    for k in range(0,9,3):
        box_list = []       #3X3의 숫자들을 담는 리스트
        
        for i in range(3):
            for j in range(3):
                box_list.append(arr[k+i][k+j]) #박스에 있는 값들 저장
        
        if set(box_list) != num_set:
            return 0
    
    return 1

T = int(input())

for t in range(1,T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{t} {sdoku(arr)}')