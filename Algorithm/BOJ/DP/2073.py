import sys
sys.stdin = open('DP/input.txt','r')

'''
7 6
4 5
3 6
2 7
1 4
6 7
1 5
'''

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

D, P = map(int, input().split())

for _ in range(P):
    L, C = map(int, input().split())

    