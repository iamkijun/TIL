import sys
sys.stdin = open("Graph/input.txt","r")
'''
6 4
0100
1110
1000
0000
0111
0000
'''
N, M = map(int, input().split())

arr = [['1']* (M+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']* (M+2)]

si, sj = 1, 1

fi, fj = N, M