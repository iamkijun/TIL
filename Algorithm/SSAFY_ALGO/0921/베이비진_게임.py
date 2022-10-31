import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = list(map(int, input()))

    li = [0] * 10

    for i in range(len(S)):
        li[S[i]] += 1

    while True:
        if max(li) >= 3:
            li[li.index(max(li))] -= 3
        else:
            break

    for i in range(8):
        if li[i:i+3] == [1,1,1]:
            li[i] = 0
            li[i+1] = 0
            li[i+2] = 0

    if sum(li) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')