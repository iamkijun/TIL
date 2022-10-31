import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N= int(input())

    arr = []

    for _ in range(N):
        a = list(map(int, input().split()))
        arr.append(a)

    count = 1

    i =0

    if N>2:
        while i <= N-2:
            if arr[i][1] > arr[i+1][0]:
                count+=1
                arr.pop(i)
                N-=1
            else:
                i += 1

    elif N == 2:
        if arr[0][1] > arr[1][0]:
            count+=1
        else:
            pass

    print(f'#{t} {count}')
