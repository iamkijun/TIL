import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())

    q = list(map(int, input().split()))


    count = 0 #다 녹은 피자의 수
    cnt= 0
    while True:

        for j in range(M):
            q.append(q.pop(0)//2)
            if q.count(0) == M-1:
                print("<<<<<<<<<<<",q,q.index(1)+j)
                break

        print(q)

        if q.count(0) == M - 1:
            break


    print(f'#{t}')