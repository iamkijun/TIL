import sys
sys.stdin = open('IM추천문제/input.txt','r')

def max_len(arr):
    for k in range(100,0,-1):
        for i in range(100):
            for j in range(101-k):
                    if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                        return k


for t in range(1,11):
    T = int(input())

    arr = [list(map(str, input())) for _ in range(100)]

    # [1] 행의 최대 길이
    a = max_len(arr)
    
    # [2] 전치행렬
    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # [3] 열의 최대 길이
    b = max_len(arr)

    if a >= b:
        print(f'#{T} {a}')
    elif b > a:
        print(f'#{T} {b}')