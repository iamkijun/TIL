import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    arr = list(map(int, input().split()))
    ans = 0
    
    
    for i in range(1<<10):
        total = 0
        for j in range(10):
            if i & (1<<j):
                total += arr[j]
                if total == 0:
                    ans = 1
                    break
                else:
                    pass

    print(f'#{t} {ans}')