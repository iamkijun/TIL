import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnts = [0] * 5001 #정류장의 개수

    for _ in range(N):
        S, E = map(int,input().split())
        for i in range(S, E+1):
            cnts[i] += 1

    P = int(input())

    sols = []
    for _ in range(P):
        n = int(input())
        sols.append(cnts[n])

    print(f'#{t}', *sols)