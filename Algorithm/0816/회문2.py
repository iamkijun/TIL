import sys
sys.stdin = open("input.txt","r")

def one(arr):
    maxl = 0

    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(101-k):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    return k


def two(arr):
    arr = list(zip(*arr))  # 전치행렬

    maxl = 0
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(101-k):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    return k


for _ in range(10):
    N = int(input())

    arr = [list(map(str,input())) for _ in range(100)]

    v1 = one(arr)
    v2 = two(arr)

    if v1 >= v2:
        print(f'#{N} {v1}')
    else:
        print(f'#{N} {v2}')

