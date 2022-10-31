# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    li = list(map(int,input()))

    maxV = 0
    count = 0
    for i in range(N):
        if li[i] == 1:
            count +=1
            if count > maxV:
                maxV = count
        else:
            count = 0

    print(f'#{t} {maxV}')