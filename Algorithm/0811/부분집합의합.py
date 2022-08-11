import sys
sys.stdin = open("input.txt", "r")

A = []

for i in range(1,13):
    A.append(i)

T = int(input())

for t in range(1,T+1):
    N, K = map(int, input().split())

    count = 0
    for i in range(1,1<<12):
        total = 0
        total_list = []
        for j in range(12):
            if i & (1<<j):
                total += A[j]
                total_list.append(A[j])

        if len(total_list) == N:
            if total == K:
                count += 1

    print(f'#{t} {count}')