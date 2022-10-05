'''
5 8 3
2 4 5 4 6
'''

import sys
sys.stdin = open('input.txt','r')

N, M, K = map(int, input().split())
N_li = list(map(int,input().split()))

N_li.sort()


max_val = N_li[-1]
second_val = N_li[-2]

'''
단순한 풀이
ans = 0
cnt = 0
for _ in range(M):
    if cnt < K:
        ans += max_val
        cnt += 1
    elif cnt == K:
        ans += second_val
        cnt = 0

print(ans)
'''

# Fancy한 풀이
# 가장 큰 수가 더해지는 횟수
count = M//(K+1) * K
count += M % (K+1)

ans = 0
ans += max_val * count
ans += second_val * (M-count)

print(ans)