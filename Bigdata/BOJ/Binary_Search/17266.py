import sys
sys.stdin = open('Binary_Search/input.txt','r')

N = int(input())

M = int(input())

M_li = list(map(int, input().split()))
M_li.sort(reverse=True)
max_val = 0
for i in range(M-1):
    max_val = max(max_val, M_li[i]-M_li[i+1])

ans = max((max_val+1)//2,M_li[-1],N-M_li[0])

print(ans)