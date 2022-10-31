import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())

arr = [[] for _ in range(N)]
max_b = 0
max_idx = 0
max_cnt = 0
max_b = 0
max_idx = 0

for i in range(N):
    a, b = map(int, input().split())

    if b >= max_b:
        if b > max_b:
            max_cnt = 1
        elif b == max_b:
            max_cnt += 1
        max_b = b
        max_idx = i
        
    arr[i] = [a,b]

current_max = 0
current_min = 0

cnt = 0

if max_cnt == 1:
    for i in range(N):
        if arr[i][b] > current_max:
            current_max = arr[i][b]
            cnt +=1
        if max_b == current_max:
            current_min = arr[i][b]
            break
    for j in range(max_idx+1,N):
        if arr[j][b] < current_min:
            current_min = arr[j][b]
            cnt +=1
    
elif max_cnt >=1:
    for i in range(N):
        if arr[i][b] > current_max:
            current_max = arr[i][b]
            cnt +=1
        if max_b == current_max:
            current_min = arr[i][b]
            cnt +=1
            break
    for j in range(max_idx+1,N):
        if arr[j][b] < current_min:
            current_min = arr[j][b]
            cnt +=1

print(cnt)
    
    