import sys
sys.stdin = open("D4/sample_input.txt","r")

for t in range(1,11):
    N = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for i in range(1,101):
        if arr[99][i] == 2:
            idx = i

    j = 99
    while j != 0:
        if arr[j][idx-1] == 1:
            arr[j][idx] = 0
            idx = idx -1
        elif arr[j][idx+1] == 1:
            arr[j][idx] = 0
            idx = idx +1
        else:
            arr[j][idx] = 0
            j = j - 1

    print(f'#{N} {idx-1}')