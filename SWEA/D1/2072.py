T =int(input())

for i in range(1,T+1):
    l = map(int, input().split())
    l = list(l)
    odd_list = []
    for j in range(10):
        if l[j] % 2 == 1:
            odd_list.append(l[j])

    sum_odd = sum(odd_list)
    print(f'#{i} {sum_odd}')