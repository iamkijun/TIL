import sys
sys.stdin = open('input.txt','r')

n = int(input())

li = list(map(int, input().split()))

x = int(input())

li.sort()

cnt = 0

left = 0
right = n-1

while left < right:
    if li[left]+li[right] > x:
        right -=1
    elif li[left]+li[right] < x:
        left += 1
    else:
        cnt+= 1
        left += 1
        right -= 1
    
print(cnt)