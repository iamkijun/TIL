import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):

    a, b = map(int, input().split())

    if a + b >= 24:
        print(f'#{t} {a+b-24}')
    else:
        print(f'#{t} {a+b}')