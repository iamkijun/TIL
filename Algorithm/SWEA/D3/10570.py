import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):
    A, B = map(int, input().split())
    count = 0

    for i in range(A,B+1):
        i_str = str(i)
        i_reverse = i_str[::-1]

        i_sqrt= i**0.5
        i_sqrt_reverse = str(int(i_sqrt))[::-1]

        if i_str == i_reverse and i_sqrt == float(i_sqrt_reverse):
            count+=1

    print(f'#{t} {count}')