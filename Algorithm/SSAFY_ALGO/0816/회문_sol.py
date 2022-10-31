import sys
sys.stdin = open("input.txt","r")

def solve(arr):
    #행
    for _ in range(2):
        for lst in arr:
            for i in range(N-M+1):
                if lst[i:i+M] == lst[i:i+M][::-1]:
                    return lst[i:i+M]
        arr = list(zip(*arr))

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve(arr)

    print(f'#{t}',end=" ")
    print(''.join(ans))