import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):

    N = int(input())

    li = list(map(int, input().split()))

    min_V = 0
    max_V = 0

    for i in range(N-1):
        if li[i] < li[i+1]:
            if max_V < li[i+1] - li[i]:
                max_V = li[i+1] - li[i]
        elif li[i] > li[i+1]:
            if min_V < li[i] - li[i+1]:
                min_V = li[i] - li[i+1]

    print(f'#{t} {max_V} {min_V}')