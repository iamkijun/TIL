import sys
sys.stdin = open('input.txt','r')

w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

#[x좌표]
dj =1
count = 0
while count < t%(2*w):
    if 0 <= p+dj <= w:
        pass
    else:
        dj *= -1
    
    p = p+dj

    count +=1

#[y좌표]
di =1
count= 0
while count < t%(2*h):
    if 0 <= q + di <= h:
        pass
    else:
        di *= -1
            
    q = q+di
    
    count +=1

print(p ,q)
