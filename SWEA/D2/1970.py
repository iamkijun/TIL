T = int(input())

for i in range(1,T+1):
    print(f'#{i}')
    N = int(input())
    
    li = [50000,10000,5000,1000,500,100,50,10]

    val = []

    for j in range(8):
        if N // li[j] > 0:
            a = str(N // li[j])
            val.append(a)
        elif N // li[j] == 0:
            val.append('0')

        N = N % li[j]
    
    print(' '.join(val))