import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for t in range(1,T+1):
    li = list(map(int, input().split()))

    count = 0

    for i in range(1<<len(li)):
        total=0
        for j in range(len(li)):
            if i & (1<<j):
                total += li[j]
                if total == 0:
                    count += 1
                else:
                    pass
    if count > 0:
        result = 1
    else:
        result = 0


    print(f'#{t} {result}')