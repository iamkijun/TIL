T = int(input())

for i in range(1,T+1):
    N = int(input())
    count = 0
    list = []
    for j in [2,3,5,7,11]:
        while True:
            if N % j == 0:
                count +=1
                N = N // j
            else:
                list.append(count)
                count = 0
                break

    print(f'#{i} {list[0]} {list[1]} {list[2]} {list[3]} {list[4]}')