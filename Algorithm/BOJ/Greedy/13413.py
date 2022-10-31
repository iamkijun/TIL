import sys
sys.stdin = open("Greedy/input.txt","r")

T = int(input())

for t in range(1,T+1):

    N = int(input())

    cnt = 0
    for _ in range(2):
        S = list(input())
        print(S)

        for i in range(1,N-1):
            if S[i] == 'B':
                if S[i-1] == 'W' and S[i+1] == 'W':
                    pass
                

    print(cnt)