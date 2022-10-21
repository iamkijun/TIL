import sys
sys.stdin = open('input.txt','r')

H, W = map(int, input().split())

arr = [list(map(str, input())) for _ in range(H)]

#초기값: 비안오는 날로 생각해 -1로 세팅
ans = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        for k in range(W-j):    #비가 오는 좌표에서 오른쪽 싹 다 +1씩
            if arr[i][j] == 'c':
                ans[i][j+k] = k

for i in range(H):
    print(*ans[i])