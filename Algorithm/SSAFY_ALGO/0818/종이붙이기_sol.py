import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1,T+1):
    N = int(input())//10
    lst = [0]*(N+1)
    if N>=1:
        lst[1] = 1
    if N>=2:
        lst[2] = 3
    if N >= 3:
        for i in range(3, N+1):
            lst[i] = lst[i-1] + lst[i-2] * 2

    print(f'#{t} {lst[N]}')