import sys
sys.stdin = open('input.txt','r')

T = int(input())

def backtracking(i,j):
    global ans

    if len(ans) == 7:
        if ans not in ans_list:
            ans_list.append(ans)
        return

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):

        ni, nj = i+di, j+dj

        if 0<=ni<4 and 0<=nj<4:             #범위 안에 있으면

            ans += arr[ni][nj]
            backtracking(ni,nj)
            ans = ans[:-1]

        else:
            continue

for t in range(1,T+1):

    arr = [list(input().split()) for _ in range(4)]

    ans_list = []

    for i in range(4):
        for j in range(4):

            ans = arr[i][j]

            backtracking(i,j)

    print(f'#{t} {len(ans_list)}')