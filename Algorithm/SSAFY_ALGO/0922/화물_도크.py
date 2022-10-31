import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    li = []
    for i in range(N):
        s, e = map(int, input().split())
        li.append([s,e])

    li = sorted(li,key = lambda x:x[1])

    cnt =1
    last = li[0][1]
    idx = 1
    while idx<N:
        if li[idx][0]>=last:
            last = li[idx][1]
            cnt+=1
        idx +=1

    print(f'#{t} {cnt}')