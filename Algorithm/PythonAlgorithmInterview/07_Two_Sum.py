nums = list(map(int, input().split()))

target = int(input())

#### 1. 브루트포스 (시간복잡도 n^2)
# def twoSum(li,val):
#     for i in range(len(li)-1):
#         for j in range(i+1,len(li)):
#             if li[i] + li[j] == val:
#                 return [i, j]

# print(twoSum(nums,target))

#### 2. in을 이용한 탐색 
# def twoSum(li,val):
#     for i, n in enumerate(li):
#         left = val - n

#         if left in li[i+1:]:
#             return [i, li.index(left)]

# print(twoSum(nums,target))

#### 3. 첫번째 수를 뺀 결과 키 조회
# def twoSum(li, val):
#     nums_map = {}
#     #키:값, 값:키로 저장하여 딕셔너리에 저장 
#     for i, num in enumerate(li):
#         nums_map[num] = i

#     #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#     for i, num in enumerate(li):
#         if val - num in nums_map and i != nums_map[val-num]:
#             return [i, nums_map[val-num]]

# print(twoSum(nums,target))
