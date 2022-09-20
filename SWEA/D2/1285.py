import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for i in range(1,T+1):
    N = int(input())
    a= list(map(int, input().split()))
    min = 100000
    count = 0
    for val in a:
        if abs(val) < min:
            min = abs(val)
            count = 1
        elif abs(val) == min:
            count += 1
        
    print(f'#{i} {min} {count}')