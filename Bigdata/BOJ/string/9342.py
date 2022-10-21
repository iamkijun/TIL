import sys
sys.stdin = open('String/input.txt','r')

T = int(input())

for t in range(T): 
    S = list(input())

    atof = ['A','B','C','D','E','F']
    idx = 0

    if S[idx:].count('A') >= 1:
        idx = S.index('A')
        pass
    else:
        print('Good')
        continue

    if S[idx:].count('F') >= 1:
        idx = S.index('F')
        pass
    else:
        print('Good')
        continue

    if S[idx:].count('C') >= 1:
        idx = S.index('C')
        pass
    else:
        print('Good')
        continue

    if S[idx+1:] in 