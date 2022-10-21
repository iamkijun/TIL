N, M = map(int, input().split())

n_list = list(map(int, input().split()))

sum_list = []

min=M
remember_min = 0

for i1 in n_list:
    for i2 in n_list:
        if i1 != i2:
            for i3 in n_list:
                if i3 != i1 and i3 != i2:
                    sum_value = i1+i2+i3 
                    if sum_value <= M:             
                        if M - sum_value< min:
                            min = abs(sum_value - M)
                            remember_min = sum_value
                            if min == 0:
                                break

print(remember_min)