import sys
sys.stdin = open('input.txt','r')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

team = []
for i in range(N):
    for j in range(N):
        