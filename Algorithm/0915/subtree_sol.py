import sys
sys.stdin = open('input.txt','r')
#
T = int(input())

def postorder(n):
    global cnt

    if n == 0:
        return
    postorder(ch1[n])
    postorder(ch2[n])
    cnt+=1

for t in range(1,T+1):
    E, S = map(int,input().split())

    li = list(map(int, input().split()))

    # [1] 트리를 저장: ch1, ch2
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    for i in range(0, 2*E, 2):
        p, c = li[i], li[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0

    postorder(S)

    print(f'#{t} {cnt}')