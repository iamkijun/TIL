import sys
sys.stdin = open("s_input.txt","r")

for i in range(1, 11):
    N = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for j in range(2,N-2):
        if a[j] > a[j-1] and a[j] > a[j-2] and a[j] > a[j+1] and a[j] > a[j+2]:
            if a[j-2]>= a[j-1] and a[j-2] >= a[j+1] and a[j-2] >= a[j+2]:
                cnt += a[j] - a[j-2]
            elif a[j-1] >= a[j-2] and a[j-1] >= a[j+1] and a[j-1] >= a[j+2]:
                cnt += a[j] - a[j-1]
            elif a[j+1] >= a[j-2] and a[j+1] >= a[j-1] and a[j+1] >= a[j+2]:
                cnt += a[j] - a[j+1]
            elif a[j+2] >= a[j-2] and a[j+2] >= a[j-1] and a[j+2] >= a[j+1]:
                cnt += a[j] - a[j+2]

    print(f'#{i} {cnt}')