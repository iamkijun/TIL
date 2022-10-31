import sys
sys.stdin = open("input.txt")

def backtracking(n):
    global ans

    if n == N:
        ans +=1
        return

    for j in range(N):
        if j not in visited1 and (n+j) not in visited2 and (n-j) not in visited3:
            visited1.append(j)
            visited2.append(n+j)
            visited3.append(n-j)
            backtracking(n+1)
            visited1.pop()
            visited2.pop()
            visited3.pop()


N = int(input())

# arr = [[0] * N for _ in range(N)]
ans = 0

visited1 =[] #열 중복 방지
visited2 =[] #/ 대각선 방지
visited3 =[] #\ 대각선 방지

backtracking(0)

# print(f'#{t} {ans}')

print(ans)