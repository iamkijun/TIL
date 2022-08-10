import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1,T+1):

    N = int(input())

    li=[]

    for _ in range(N):
        AB= list(map(int, input().split()))
        li.append(AB)

    P = int(input())

    C_list = [0] * (P+1)

    for i in range(N):
        for j in range(2):
            C_list[li[i][j+1]] += 1


    print(li)

    for i in range(P):
        C = int(input())

    print(f'#{t}')