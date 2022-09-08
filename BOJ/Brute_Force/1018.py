import sys
sys.stdin = open('Brute_Force/input.txt','r')

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]
cnt = 64

for a in range(N-7):
    for b in range(M-7):
        cnt1 = 0
        cnt2 = 0

        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i + j) % 2 == 0:
                    if arr[i][j] == 'W':
                        cnt1 += 1
                    elif arr[i][j] == 'B':
                        cnt2 += 1
                elif (i + j) % 2 == 1:            
                    if arr[i][j] == 'B':
                        cnt1 += 1
                    if arr[i][j] == 'W':
                        cnt2 += 1

        cnt_min = min([cnt1,cnt2])
        if cnt_min < cnt:
            cnt = cnt_min

print(cnt)