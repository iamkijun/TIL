import sys
# input = sys.stdin.readline
sys.stdin = open('Sort/input.txt','r')

N = int(input())

l = []
for i in range(N):
    a = list(input().split())
    l.append(a+[i])

l.sort(key = lambda x: (int(x[0]), x[2]))

for val in l:
    print(*val[:-1])