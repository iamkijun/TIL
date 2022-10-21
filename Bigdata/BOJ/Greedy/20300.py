import sys
sys.stdin = open('Greedy/input.txt','r')

N = int(input())

li = list(map(int, input().split()))

li.sort()
if N % 2 == 1:
    max_val = li.pop(-1)
else:
    max_val =  0

while li:
    if li[0] + li[-1] > max_val:
        max_val = li[0]+li[-1]
    
    li.pop(0)
    li.pop(-1)

print(max_val)

