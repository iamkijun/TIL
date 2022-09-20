T = int(input())

for i in range(1,T+1):
    a, b, c, d = map(int, input().split())
    if b + d < 60:
        if a + c < 13:
            print(f'#{i} {a+c} {b+d}')
        elif a + c >= 13:
            print(f'#{i} {a+c-12} {b+d}')
    elif b + d >= 60:
        if a + c < 13:
            print(f'#{i} {a+c+1} {b+d-60}')
        elif a + c >= 13:
            print(f'#{i} {a+c-11} {b+d-60}')
