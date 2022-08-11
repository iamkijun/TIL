import sys
sys.stdin = open("input.txt", "r")

for t in range(1,4):
    N= int(input())
    arr = [[0] * 102] + [[0] + list(map(int, input().split())) +[0] for _ in range(100)] + [[0] * 102]
    
    for k in range(102):
        if arr[100][k] == 2:
            remember = k
    
    row = 99
    while True:
        if row == 1:
            break


        elif arr[row][remember+1] == 1:
            while True:
                remember += 1
                if arr[row][remember+1] == 0:
                    break
        
        elif arr[row][remember-1] ==1:
            while True:
                remember -=1
                if arr[row][remember-1] == 0:
                    break

        row -=1
        
    print(f'#{t} {remember-1}')