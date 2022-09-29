import sys
sys.stdin = open('String/input.txt','r')

g, s = map(int, input().split())

G = list(input())
S = tuple(input())

from itertools import permutations

count = 0
for i in permutations(G,g):

    if i<S:
        count+=1

print(count)
