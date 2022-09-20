import sys
sys.stdin = open('input.txt','r')

T= int(input())

for t in range(1,T+1):

    N = int(input())

    li=[]

    li.append(N // 50000)
    N = N % 50000

    li.append(N // 10000)
    N =N % 10000

    li.append(N // 5000)
    N =N % 5000

    li.append(N // 1000)
    N =N % 1000

    li.append(N // 500)
    N =N % 500

    li.append(N // 100)
    N =N % 100

    li.append(N // 50)
    N =N % 50

    li.append(N // 10)

    print(f'#{t}')
    print(*li)
