import sys
sys.stdin = open('input.txt','r')
#
def preorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    preorder(ch1[node])
    preorder(ch2[node])


T = int(input())

for t in range(1,T+1):
    E, N = map(int, input().split())

    li = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E + 2)

    for i in range(E):
        if ch1[li[2*i]] == 0:
            ch1[li[2*i]] = li[2*i+1]
        else:
            ch2[li[2*i]] = li[2*i+1]

    visited = [0] * (E + 2)

    cnt = 0

    preorder(N)

    print(cnt)