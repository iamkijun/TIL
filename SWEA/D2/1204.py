T = int(input())

for i in range(T):
    num = int(input())
    
    b = map(int, input().split())
    a = list(b)
    
    li =[]
    count_li =[]
    
    for j in range(len(a)):
        if a[j] in li:
            k = li.index(a[j])
            count_li[k] += 1
            continue
        else:
            li.append(a[j])
            count_li.append(1)
    
    max_index = count_li.index(max(count_li))
    max_value = li[max_index]
    
    print(f'#{num} {max_value}')