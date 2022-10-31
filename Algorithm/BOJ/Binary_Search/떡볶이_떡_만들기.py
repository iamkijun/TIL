N, M = map(int, input().split())

N_li = list(map(int, input().split()))
N_li.sort()

s= 0
e =N_li[-1]

while s<=e:
    mid = (s+e)//2

    total = 0
    for val in N_li:
        if val > mid:
            total += (val - mid)
    
    if total > M:
        s = mid + 1
    elif total < M:
        e = mid - 1
    else:
        break
print(mid)