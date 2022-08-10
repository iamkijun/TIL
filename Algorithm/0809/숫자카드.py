import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1):

    N = int(input())
    a = list(input())

    num_li = [0] * 10
    #0 ~ 9 까지 개수 세는 리스트

    #1의 자리에 해당하는 숫자에 해당하는 리스트에 1씩 더하기
    for j in range(N):
        num_li[int(a[j])] +=1

    count = num_li[num_li.index(max(num_li))] # 횟수
    maxV = num_li.index(max(num_li)) #값

    if num_li.count(max(num_li)) >= 2:
        for j in range(9,-1,-1):
            if num_li[j] == max(num_li):
                maxV = j
                break

    print(f'#{i} {maxV} {count}')

    # for k in range(10):
    #     if num_li[k] > count: # 횟수가 클 경우 count, maxV값 불러오
    #         count = num_li[k]
    #         maxV = k
    #     elif num_li[k] == count: # 횟수가 같을 경우 큰값 도출
    #         if k > maxV:
    #             maxV = k

    # print(f'#{i} {maxV} {count}')