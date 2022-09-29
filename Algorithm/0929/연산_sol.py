from ast import operator
import sys
sys.stdin = open('0928/input.txt','r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] * (2 * M)

    q = []
    q.append([N, 0])