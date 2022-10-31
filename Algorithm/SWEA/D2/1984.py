import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for t in range(1, T+1):
    
    n = list(map(int,input().split()))

    for i in range(10):
        for j in range(i,10):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    n= n[1:-1]
    sum = 0
    for i in range(8):
        sum += n[i]

    print(f'#{t} {round(sum/8)}')
