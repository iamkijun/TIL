import sys
sys.stdin = open('input.txt','r')

T = int(input())

def binary_search(target):
    global cnt
    global li

    start = 0
    end = N-1

    while start <= end:

        mid = (start + end) // 2

        if N_li[mid] == target:
            if len(li) <= 1:
                cnt +=1

            else:
                for i in range(len(li)-1):
                    if li[i] == li[i+1]:
                        break
                else:
                    cnt+=1

            return # 함수를 끝내버린다.

        elif N_li[mid] < target:
            start = mid + 1
            li.append('l')

        elif N_li[mid] > target:
            end = mid - 1
            li.append('r')

    return cnt

for t in range(1,T+1):

    N,M = map(int, input().split())

    N_li = list(map(int, input().split()))
    N_li.sort()

    M_li = list(map(int, input().split()))
    cnt = 0

    for val in M_li:
        li = []
        binary_search(val)

    print(f'#{t} {cnt}')