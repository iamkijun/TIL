import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    N = int(input())

    li = list(map(int, input().split()))

    for j in range(N-1,0,-1):
        for k in range(0,j):
            if li[k] > li[k+1]:
                li[k], li[k+1] = li[k+1], li[k]
                #오름차순 정

    for v in range(N):
        li[v]= str(li[v])
        #li 안의 원소를 문자열로 바꿔주는 과정(join쓰기위해)

    print(f'#{i} {" ".join(li)}')