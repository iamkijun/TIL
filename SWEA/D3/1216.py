import sys
sys.stdin = open("input.txt","r")

for t in range(1,11):
    N= int(input())
    l = [list(map(str, input())) for _ in range(100)]

    cnt=0

    for i in range(100):
        for j in range(99-):
            for k in range(2,)
            if l[i][j:j+N] == l[i][::-1][100-j-N:100-j]:
                cnt +=1
    
    for i in range(100):
        for j in range(100):
            if i < j:
                l[i][j], l[j][i] = l[j][i], l[i][j]

    for i in range(100):
        for j in range(99):
            if l[i][j:j+N] == l[i][::-1][100-j-N:100-j]:
                cnt +=1


    print(f'#{N} {cnt}')
