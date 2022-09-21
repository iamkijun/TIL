import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    j_list = []
    for i in range(N):

        while True:
            if arr[i].index(min(arr[i])) in j_list:
                arr[i][arr[i].index(min(arr[i]))] = 10
            else:
                break

        total += min(arr[i])
        j_list.append(arr[i].index(min(arr[i])))


    print(f'#{t} {total}')