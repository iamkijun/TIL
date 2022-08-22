import sys
sys.stdin = open("input.txt","r")

# 11047

# N, K = map(int, input().split())
# li = []
# for i in range(N):
#     coin = int(input())
#     li.append(coin)

# count = 0

# for j in range(N-1,-1,-1):
#     if K >= li[j]:
#         count = count + (K//li[j])
#         K = K % li[j]

# print(count)

# 2839

# N = int(input())

# count = 0

# while True:
#     if N % 5 == 0:
#         count += N // 5
#         break
#     else:
#         if N<=2:
#             print(-1)
#             count = 0
#             break
#         N = N - 3
#         count += 1

# if count == 0:
#     pass
# else:
#     print(count)


# 2217

N = int(input())

W_list = []

for i in range(N):
    W = int(input())
    W_list.append(W)

W_list.sort(reverse = True)

max = 0
sum = 0
for i in range(N):
    sum = min(W_list[:(i+1)])*(i+1)
    if sum > max:
        max = sum
    
print(max)