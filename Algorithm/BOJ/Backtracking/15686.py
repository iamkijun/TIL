import sys
sys.stdin = open('Backtracking/input.txt','r')

'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 0: 빈칸, 1: 집, 2: 치킨집
