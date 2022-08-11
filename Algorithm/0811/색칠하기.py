import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):
    arr= [[0]*10 for _ in range(10)]
    cnt = 0
    N = int(input())

    for i in range(N):
        li = list(map(int,input().split()))
        for j in range(li[2]-li[0]+1):
            for k in range(li[3]-li[1]+1):
                arr[li[0]+j][li[1]+k] +=1

    for j in range(10):
        for k in range(10):
            if arr[j][k] ==2:
                cnt += 1
    
    print(f'#{t} {cnt}')