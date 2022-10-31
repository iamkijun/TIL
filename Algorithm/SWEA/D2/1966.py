T = int(input())

for i in range(1,T+1):
    N = int(input())

    a = list(map(int, input().split()))

    a.sort()

    for j in range(len(a)):
        a[j] = str(a[j])
    
    a= ' '.join(a)
    print(f'#{i} {a}')