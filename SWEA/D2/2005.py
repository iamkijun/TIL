T = int(input())

for i in range(1, T+1):
    
    n = int(input())

    print(f'#{i}')

    first =[1]
    second = [1, 1]
    total = [first,second]
    for i in range(n):
        print("\n")
        for j in range(len(total[i])):
            
            print(total[i][j], end= " ")
        