import sys
sys.stdin = open('SAMSUNG/input.txt','r')

N = int(input())

li = list(map(int,input().split()))

B, C = map(int, input().split())

for i in range(N):
    li[i] = li[i]- B

cnt = N

for val in li:
    if val > 0:
        if val % C == 0:
            cnt += (val//C)
        else:
            cnt += (val//C)+1

print(cnt)