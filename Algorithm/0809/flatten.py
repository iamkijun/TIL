import sys
sys.stdin = open("input.txt", "r")

for t in range(1,11):
    dump = int(input())

    li = list(map(int, input().split()))

    for i in range(dump):
        li.sort()
        li[0] += 1
        li[-1] -= 1
        if li[-1] - li[0] <= 1:
            break

    li.sort()
    diff = li[-1] - li[0]

    print(f'#{t} {diff}')