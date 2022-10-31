import sys
sys.stdin = open('input.txt','r')

T = int(input())

def finding(N):
    s= 1
    e= 10**18

    while s<= e:
        m = (s+e) //2
        if m**3 == N:
            return m
        elif m**3 > N:
            e = m-1
        elif m**3 < N:
            s = m+1

    return -1
for t in range(1,T+1):
    N = int(input())

    print(f'#{t} {finding(N)}')

