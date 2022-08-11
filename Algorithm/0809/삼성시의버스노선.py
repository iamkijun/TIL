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
    P_count = [0] * P

    C =[]
    for _ in range(P):
        C_el = int(input())
        C.append(C_el)

    for i in range(N):
        if li[i][0]<= C[i] <= li[i][1]:
            for j in range(li[i][0]-1,li[i][1]):
                P_count[j] += 1

    print(f'#{t}',*P_count)