import sys
sys.stdin = open("s_input.txt","r")

T = int(input())

for i in range(1,T+1):
    N = int(input())
    a= list(map(int, input().split()))

    maxV = a[0]
    minV = a[0]
    for j in range(1, N):
        if a[j] > maxV:
            maxV = a[j]
        if a[j] < minV:
            minV = a[j]

    print(f'#{i} {maxV-minV}')