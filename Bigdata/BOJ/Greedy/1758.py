import re
import sys
sys.stdin = open('Greedy/input.txt','r')

N = int(input())

num_li = [0] * N

for i in range(N):
    num_li[i] = int(input())

num_li.sort(reverse=True)

ans = 0
for j in range(N):
    if num_li[j] > j:
        ans += (num_li[j] - j)
    else:
        break

print(ans)