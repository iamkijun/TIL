import sys
sys.stdin = open('input.txt','r')

def merge_sort(arr):
    global cnt

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2                 # 반을 나눠서 각각 정렬
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    #정답 카운트 확인 low_arr[-1] > high_arr[-1]
    if low_arr[-1] > high_arr[-1]:
        cnt+=1

    #좌우 더 작은 값을 하나씩 추가
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += (low_arr[l:] + high_arr[h:])
    return merged_arr


T = int(input())

for t in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    cnt = 0
    li = merge_sort(li)

    print(f'#{t} {li[N//2]} {cnt}')