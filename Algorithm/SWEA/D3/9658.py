import sys
sys.stdin = open("D3/input.txt")

TC = int(input())

for t in range(1,TC+1):

    N = int(input())

    count = 0
    while round(N) >=10:
        N = N/10
        count +=1

    print(f'#{t} {N:.1f}*10^{count}')
