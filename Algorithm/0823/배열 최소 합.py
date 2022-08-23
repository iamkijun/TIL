import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    p = []
    d = []
    for i in range(N):
        min_v=li[i][0]
        min_idx = 0

        for j in range(1,N):
            if li[i][j] < min_v:
                for k in range(len(p)):
                    if p[k] != j:
                        pass
                    else:
                        break
                else:
                    min_v = li[i][j]
                    min_idx = j
        cnt = 0
        for k in range(N):
            if li[i][k] == min_v:
                cnt +=1

        if cnt > 1:
            d.append(i)
            continue

        total += min_v
        p.append(min_idx)


    for val in d:
        min_v=li[val][0]
        min_idx = 0

        for j in range(1,N):
            if li[val][j] < min_v:
                for k in range(len(p)):
                    if p[k] != j:
                        pass
                    else:
                        break
                else:
                    min_v = li[val][j]
                    min_idx = j

        total += min_v
        p.append(min_idx)


    print(f'#{t} {total}')