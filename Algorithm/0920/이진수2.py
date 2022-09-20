import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N = float(input())

    i = 1
    ans = ''

    while True:

        if N > (2**((-1)*i)):
            ans += '1'
            N -= (2**((-1)*i))
        elif N == (2**((-1)*i)):
            ans += '1'
            break
        else:
            ans += '0'

        i += 1

        if i == 13:
            ans = 'overflow'
            break

    print(f'#{t} {ans}')
