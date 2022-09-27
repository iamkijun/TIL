import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    li = list(map(int, input().split()))

    N = li[0]

    i = 1       # 현재 인덱스
    cnt =0      # 교체 횟수

    while True:
        until = []

        for k in range(1,li[i]+1):
            if i+k <N-1:
                until.append(i+li[i+k])

        until.sort(reverse = True)

        if until:
            i = until[0]
        else:
            i += 1

        if i >= N:
            break

        cnt += 1

    print(f'#{t} {cnt}')