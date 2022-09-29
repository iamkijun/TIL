def solution(n):
    n_li = []
    while True:
        n_li.append(str(n%10))
        n = n//10
        if n == 0:
            break
    n_li.sort(reverse = True)
    a = ''.join(n_li)
    return int(a)