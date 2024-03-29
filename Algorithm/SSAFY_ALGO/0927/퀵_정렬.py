import sys
sys.stdin = open('input.txt','r')

T = int(input())

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

for t in range(1,T+1):
    N = int(input())

    li = list(map(int, input().split()))

    li = quick_sort(li)

    print(f'#{t} {li[N//2]}')