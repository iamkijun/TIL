import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1,T+1):
    N = int(input())

    N = N//10
    ans = 1

    if N % 2 == 1:
        for i in range(2,N,2):
            ans += 2**i

    elif N % 2 == 0:
        for j in range(1,N,2):
            ans += 2**j

    print(f'#{t} {ans}')