import sys
sys.stdin = open('input.txt','r')

N = int(input())

Q = []

for i in range(N):
    s = list(map(str,input().split()))

    if len(s) ==2:
        Q.append(s[1])
    else:
        if s[0] == 'pop':
            if Q:
                print(Q.pop(0))
            else:
                print(-1)
        elif s[0] == 'size':
            print(len(Q))
        elif s[0] == 'empty':
            if Q:
                print(0)
            else:
                print(1)
        elif s[0] == 'front':
            if Q:
                print(Q[0])
            else:
                print(-1)
        elif s[0] == 'back':
            if Q:
                print(Q[-1])
            else:
                print(-1)