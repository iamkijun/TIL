n=3
m=4
x=2
y=3
r=3
c=1
k=5

answer = []
arr = ['0' * (m+1) for _ in range(n+1)]
arr[x][y] = 1
arr[r][c] = 1
count = 0
ans_list = []
def solution(n, m, x, y, r, c, k):
    global ans

    if count == k:
        ans_list.append(ans)
        return


    for di, dj in range((1,0),(0,-1),(0,1),(-1,0)):
        if 1<=x+di<=n and 1<=y+dj<=m:
            count += 1
            ni = x+di
            nj = y+dj
            if di == 1 and dj == 0:
                ans += 'd'
            elif di == 0 and dj == -1:
                ans += 'd'
            elif di == 0 and dj == 1:
                ans += 'd'
            elif di == -1 and dj == 0:
                ans += 'd'
            solution(n, m, ni, nj, r, c, k)
            count -=1
            ans = ans[:-1]



