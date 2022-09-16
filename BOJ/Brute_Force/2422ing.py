from math import comb
import sys
sys.stdin = open('Brute_Force/input.txt','r')

N, M = map(int, input().split())

arr = [[1]*N for _ in range(N)]
for x in range(M):
    a, b = map(int,sys.stdin.readline().split())
    arr[a-1][b-1] = 0
    arr[b-1][a-1] = 0

cnt = 0
from itertools import combinations

for big in combinations(range(N),3):
    if arr[big[0]][big[1]] and arr[big[1]][big[2]] and arr[big[0]][big[2]]:
        cnt += 1

print(cnt)
