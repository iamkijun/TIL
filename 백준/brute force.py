# # 2798

# N, M = map(int, input().split())

# n_list = list(map(int, input().split()))
# n_list.sort()
# sum_list = []

# min=M

# for j in range(N-2):
#     sum_value = n_list[j]+n_list[j+1]+n_list[j+2]
#     if abs(sum_value - M) < min:
#         min = abs(sum_value - M)
#         value = j
    
# print(n_list[value]+n_list[value+1]+n_list[value+2])