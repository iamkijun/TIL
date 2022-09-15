import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    li = list(map(int, input().split()))
    li.insert(0,0)

    ans = [0]
    for i in range(1,N+1):
        ans.append(li[i])
        while True:
            if ans[i] < ans[i//2]:
                ans[i], ans[i//2] = ans[i//2], ans[i]
                i= i//2
            else:
                break


    i = N
    result = 0
    while True:
        result += ans[i//2]
        i = i //2
        if i == 0:
            break

    print(f'#{t} {result}')

