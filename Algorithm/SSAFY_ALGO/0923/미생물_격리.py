import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,2):

    N, M, K = map(int, input().split())

    arr = [[[0,0] for _ in range(N)] for _ in range(N)]

    for i in range(K):

        ci, cj, num, dir = map(int, input().split())

        arr[ci][cj][0] = num
        arr[ci][cj][1] = dir

    for i in range(N):
        print(arr[i])

    print("dsaffdas")

    for m in range(M):
        for i in range(N):
            for j in range(N):
                max1 = 0
                max1_dir = 0
                for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
                    if 0<=i+di<N and 0<=j+dj<N:
                        ni = i+di
                        nj = j+dj
                    else:
                        continue

                    if arr[ni][nj][0] > 0:
                        if i == 0 and arr[ni][nj][1] == 1:
                            arr[i][j][0] = (arr[ni][nj][0]) // 2
                            arr[i][j][1] = 1

                            arr[ni][nj][0] = 0
                            arr[ni][nj][1] = 0
                            break
                        elif i == N - 1 and arr[ni][nj][1] == 2:
                            arr[i][j][0] = (arr[ni][nj][0]) // 2
                            arr[i][j][1] = 2

                            arr[ni][nj][0] = 0
                            arr[ni][nj][1] = 0
                            break
                        elif j == 0 and arr[ni][nj][1] == 3:
                            arr[i][j][0] = (arr[ni][nj][0]) // 2
                            arr[i][j][1] = 3

                            arr[ni][nj][0] = 0
                            arr[ni][nj][1] = 0
                            break
                        elif j == N - 1 and arr[ni][nj][1] == 4:
                            arr[i][j][0] = (arr[ni][nj][0]) // 2
                            arr[i][j][1] = 4

                            arr[ni][nj][0] = 0
                            arr[ni][nj][1] = 0
                            break
                        else:

                            if di == -1 and dj == 0 and arr[ni][nj][1] == 2:
                                pass
                            elif di == 1 and dj == 0 and arr[ni][nj][1] == 1:
                                pass
                            elif di == 0 and dj == 1 and  arr[ni][nj][1] == 3:
                                pass
                            elif di == 0 and dj == -1 and arr[ni][nj][1] == 4:
                                pass
                            else:
                                continue

                            if max1_dir == 0:
                                max1 = arr[ni][nj][0]
                                max1_dir = arr[ni][nj][1]
                            else:
                                if arr[ni][nj][0] > max1:
                                    max1 = arr[ni][nj][0]
                                    max1_dir = arr[ni][nj][1]

                            arr[i][j][0] += arr[ni][nj][0]
                            arr[i][j][1] = max1_dir

                            arr[ni][nj][0] = 0

                            arr[ni][nj][1] = 0


        total = 0
        for i in range(N):
            print(arr[i])
            for j in range(N):
                total+= arr[i][j][0]
        print("dsaffdas")

    print(f'#{t} {total}')