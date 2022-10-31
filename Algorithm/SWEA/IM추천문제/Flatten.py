import sys
sys.stdin = open('input.txt','r')

#선택정렬을 활용하여 정렬
def selection_sort(H_list):
    for i in range(99):
        min_idx = i             #첫번째 인자를 최소값의 인덱스로 선언
        for j in range(i+1, 100): #그 다음꺼부터 끝까지 비교
            if H_list[j] < H_list[min_idx]:
                min_idx = j
        H_list[min_idx], H_list[i] = H_list[i], H_list[min_idx]
    
    return H_list

for t in range(1,11):

    N = int(input())

    H_list = list(map(int, input().split()))

    # N번 덤핑
    for i in range(N):
        H_list = selection_sort(H_list)
        H_list[0] += 1
        H_list[-1] -= 1

    H_list = selection_sort(H_list) #마지막으로 정렬 한 번 더 해주기

    dif = H_list[-1] - H_list[0]    #최고점과 최저점의 높이값

    print(f'#{t} {dif}')