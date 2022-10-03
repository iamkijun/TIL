import sys
sys.stdin = open('Brute_Force/input.txt','r')

N, M = map(int, input().split())

li = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if i > M:
        continue
    elif i == M:
        cnt +=1
        continue
    
    for j in range(i,N+1):
        if sum(li[i:j]) > M:
            break
        elif sum(li[i:j]) == M:
            cnt +=1
            break
print(cnt)