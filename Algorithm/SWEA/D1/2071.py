T = int(input())

for i in range(1,T+1):
    a = list(map(int, input().split()))
    avg = sum(a)/len(a)
    print(f'#{i} {avg :.0f}')