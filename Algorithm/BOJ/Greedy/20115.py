import sys
sys.stdin = open('Greedy/input.txt','r')

N = int(input())

li = list(map(int, input().split()))

li.sort()

ans = li[-1] + sum(li[:-1])/2

if ans == int(ans):
    print(int(ans))
else:
    print(ans)
