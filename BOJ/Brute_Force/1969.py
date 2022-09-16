import sys
sys.stdin = open('Brute_Force/input.txt','r')

N, M = map(int, input().split())

arr = []
for _ in range(N):
    S = list(input())
    arr.append(S)

ans = ''
cnt = 0
for i in range(M):
    li = [0,0,0,0]
    for j in range(N):
        if arr[j][i] == 'A':
            li[0] +=1
        elif arr[j][i] == 'C':
            li[1] +=1
        elif arr[j][i] == 'G':
            li[2] +=1
        elif arr[j][i] == 'T':
            li[3] +=1

    if li.index(max(li)) == 0:
        ans += 'A'
    elif li.index(max(li)) == 1:
        ans += 'C'
    elif li.index(max(li)) == 2:
        ans += 'G'
    elif li.index(max(li)) == 3:
        ans += 'T'

    cnt += (N -max(li))



    
print(ans)
print(cnt)
