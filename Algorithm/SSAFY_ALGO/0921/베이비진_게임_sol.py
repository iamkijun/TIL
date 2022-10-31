import sys
sys.stdin = open('input.txt','r')

T = int(input())

def baby(li):
    cnt = 0
    for i in range(0, 6, 3):
        if li[i] == li[i+1] == li[i+2] or li[i] == li[i+1]+1 == li[i+2]+2:
            cnt += 1
        return cnt


def perm(n):
    global ans
    if n == 5:
        if baby(li) == 2:
            ans = 1
        return
    
    for i in range(n+1,6):
        li[i],li[n] = li[n],li[i]
        perm(n+1)
        li[i],li[n] = li[n],li[i]

for t in range(1,T+1):

    li = list(map(int, input()))

    ans = 0

    perm(0)

    print(f'#{t} {ans}')