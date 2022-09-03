import sys
sys.stdin = open('input.txt','r')

N = int(input())

li = list(map(int, input().split()))

li.sort()

left = 0
right = N-1
le, ri = li[0], li[1]
min_value = sys.maxsize
if N ==2:
    print(le,ri)
else:
    while left <right:

        if abs(li[left] +li[right]) < min_value:
            min_value = li[left]+li[right]
            le, ri = li[left], li[right]
        if min_value == 0:
            break

        if li[left+1]-li[left] > li[right]-li[right-1]:
            right -=1
        elif li[left+1]-li[left] <= li[right]-li[right-1]:
            left +=1
    print(le, ri)
    