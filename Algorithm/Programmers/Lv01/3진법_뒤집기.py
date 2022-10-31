def solution(n):
    i = 1

    while True:
        if n >=3**i:
            i+=1
        else:
            break

    li = [0]*i
    for idx in range(i):
        for k in range(2,-1,-1):
            if n >= k*(3**(i-1-idx)):
                li[idx] = k
                n -= k*(3**(i-1-idx))
                break
    li = li[::-1]

    ans = 0
    for idx in range(i):
        ans += (li[idx]*(3**(i-1-idx)))

    return ans