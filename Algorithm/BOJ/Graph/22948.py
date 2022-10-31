'''
4
1 5 4
2 3 1
3 6 1
4 13 3
2 4
'''

import sys
sys.stdin = open("Graph/input.txt","r")

N = int(input())

for n in range(N):
    k, x, r = map(int, input().split())

A, B = map(int, input().split())