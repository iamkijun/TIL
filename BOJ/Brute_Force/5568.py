from itertools import permutations
import sys

sys.stdin = open('Brute_Force/input.txt','r')


n = int(input())

k = int(input())

num_li = []
for i in range(n):
    num = input()
    num_li.append(num)

ans =set()

for a in permutations(num_li,k):
    candidate = ''.join(a)
    ans.add(candidate)

print(len(ans))