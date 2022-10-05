rain = list(map(int, input().split()))

cnt = 0
#### 1. 투 포인터를 최대로 이동
# def trap(li):
#     if not li:
#         return 0

#     cnt = 0

#     left, right = 0, len(li)-1 #인덱스
#     left_max, right_max = li[left], li[right]

#     while left < right:
#         left_max, right_max = max(left_max,li[left]), max(right_max,li[right])

#         if left_max <= right_max:
#             cnt += left_max - li[left]
#             left += 1
#         else:
#             cnt += right_max - li[right]
#             right -= 1

#     return cnt

# print(trap(rain))

#### 2. 스택 쌓기
def trap(li):
    stk = []
    volume = 0
    for i in range(len(li)):
        while stk and li[i] > li[stk[-1]]:
            top = stk.pop(-1)

        if not len(stk):
            break

        distance = i - stk[-1] -1
        

        stk.append(i)

    return volume