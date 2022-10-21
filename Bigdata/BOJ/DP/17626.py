import sys
sys.stdin = open('DP/input.txt','r')

from itertools import combinations

n = int(input())

dp = [x**2 for x in range(1,int(n**0.5))]
print(dp)

i = 0
while True:
    for a in combinations(dp, i):
        