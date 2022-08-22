import sys
sys.stdin = open('input.txt','r')

def Binary(li,end,key):
    s = 0
    e = end-1

    while s <= e:
        middle = (s+e)//2
        total = 0

        for i in range(len(li)):
            if li[i] > middle:
                total += li[i] - middle

        if total == key:
            return middle
        elif total < key:
            e = middle - 1
        else:
            s = middle + 1
    
    return middle


N, M = map(int, input().split())

H = list(map(int, input().split()))

print(Binary(H,max(H),M))

        