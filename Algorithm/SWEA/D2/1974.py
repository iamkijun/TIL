import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for t in range(1,T+1):
    
    arr = [list(map(int,input().split())) for _ in range(9)]
    num = set([1,2,3,4,5,6,7,8,9])

    count = 0

    for i in range(9):
        if set(arr[i]) == num:
            pass
        else:
            count +=1
            


    for i in range(9):
        for j in range(9):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(9):
        if set(arr[i]) == num:
            pass
        else:
            count +=1

    thxth= []
    for k in range(3):
        for i in range(3):
            for j in range(3):
                thxth.append(arr[3*k+i][3*k+j])

        if set(thxth) == num:
            pass
        else:
            count+=1


    if count == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')