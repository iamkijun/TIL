left = 1000 - int(input())

cnt = 0

if left // 500 >= 1:
    cnt += left // 500
    left = left % 500

if left // 100 >= 1:
    cnt += left // 100
    left = left % 100

if left // 50 >= 1:
    cnt += left // 50
    left = left % 50

if left // 10 >= 1:
    cnt += left // 10
    left = left % 10

if left // 5 >= 1:
    cnt += left // 5
    left = left % 5

if left >= 1:
    cnt += left

print(cnt)

