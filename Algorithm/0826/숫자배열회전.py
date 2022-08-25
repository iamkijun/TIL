import sys
sys.stdin = open('input.txt','r')

def rotate(arr):
    arrR = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[N-1-j][i]

    return arrR

T = int(input())

for t in range(1,T+1):
    print(f'#{t}')

    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr1= rotate(arr)
    arr2= rotate(arr1)
    arr3= rotate(arr2)

    for a,b,c in zip(arr1,arr2,arr3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')
    # ans = [['']*3 for _ in range(N)]            #새로운 NX3배열 생성
    #
    # for k in range(3):
    #     if k == 0:                              #90도 회전
    #         for i in range(N):
    #             a = ''                          #해당열, 밑에서부터 위로
    #             for j in range(N-1,-1,-1):
    #                 a += arr[j][i]
    #             ans[i][k] = a
    #
    #     elif k == 1:                              #180도 회전
    #         for i in range(N):
    #             a = ''
    #             for j in range(N-1,-1,-1):        #N-1-해당행, 오른쪽에서 왼쪽
    #                 a += arr[i][j]
    #             ans[N-i-1][k] = a
    #     elif k == 2:                              #270도 회전
    #         for i in range(N):
    #             a = ''
    #             for j in range(N):                #해당행, 아래서 부터 위로
    #                 a += arr[j][i]
    #             ans[N-i-1][k] = a
    # for i in range(N):
    #     print(*ans[i])

