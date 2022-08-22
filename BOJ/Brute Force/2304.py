import sys
sys.stdin = open('input.txt','r')

N = int(input())

dic= {}

for n in range(N):
    L, H = map(int, input().split())
    
    dic[L] = H

a =sorted(dic.items())

max_H = 0
area = 0
before_key = 0

for i in range(len(a)):
    if a[i][1] > max_H:
        area += max_H*(a[i][0]-before_key)
        before_key = a[i][0]
        max_H = a[i][1]
    
    if max_H == max(dic.values()):
        x = before_key
        break

max_H = 0
before_key = 0

for j in range(len(a)-1,-1,-1):
    if a[j][1] > max_H:
        area += max_H*(before_key-a[j][0])
        before_key = a[j][0]
        max_H = a[j][1]
    
    if max_H == max(dic.values()):
        y = before_key
        break

area += (y-x+1)*max(dic.values())

print(area)

