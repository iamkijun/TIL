import sys
sys.stdin = open("input.txt","r")

for t in range(1,11):
    N=int(input())
    l = [list(map(str, input())) for _ in range(8)]

    cnt=0

    for i in range(8):
        for j in range(9-N):
            if l[i][j:j+N] == l[i][::-1][8-j-N:8-j]:
                cnt +=1
    
    for i in range(8):
        for j in range(8):
            if i < j:
                l[i][j], l[j][i] = l[j][i], l[i][j]

    for i in range(8):
        for j in range(9-N):
            if l[i][j:j+N] == l[i][::-1][8-j-N:8-j]:
                cnt +=1


    print(f'#{t} {cnt}')
