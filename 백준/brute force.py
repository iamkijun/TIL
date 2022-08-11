# 2798

# N, M = map(int, input().split())

# n_list = list(map(int, input().split()))

# sum_list = []

# min=M
# remember_min = 0

# for i1 in n_list:
#     for i2 in n_list:
#         if i1 != i2:
#             for i3 in n_list:
#                 if i3 != i1 and i3 != i2:
#                     sum_value = i1+i2+i3 
#                     if sum_value <= M:             
#                         if M - sum_value< min:
#                             min = abs(sum_value - M)
#                             remember_min = sum_value
#                             if min == 0:
#                                 break

# print(remember_min)


# 2702

# a, b = map(int, input().split())
# li = []
# for i in range(a, 0, -1):
#     if a % i == 0:
#         li.append(i)
# if len(li) < b:
#     print(0)
# else:
#     print(li[-b])

# 2231
# import copy as cp

# N = int(input())

# min = N
# ver = N

# while ver!=0:
#     ver_copy = cp.deepcopy(ver)
#     ver_val = ver_copy

#     while ver_copy !=0:
#         ver_val += ver_copy%10
#         ver_copy = ver_copy//10
    
#     if ver_val == N:
#         min = ver
#     else:
#         pass
    
#     ver = ver-1
    

# if min == N:
#     print(0)
# else:
#     print(min)

# 1977
# import math 

# M = int(input())
# N = int(input())

# sum_n=0
# min_n=0

# m = math.ceil(M**0.5)
# n = math.floor(N**0.5)

# if n < m:
#     print("-1")
# else:
#     min_n = m**2
#     for i in range(n-m+1):
#         sum_n += m**2
#         m+= 1
        
#     print(sum_n)
#     print(min_n)

    
# 7568

# N = int(input())
# arr = []
# for i in range(N):
#     li = list(map(int,input().split()))
#     arr.append(li)
# rank =[]

# for i in range(N):
#     for j in range(2):
#         arr[i][j]

# 1436
# import copy
# N = int(input())
# count = 0
# a = 664

# while count < N:
#     a_copy = copy.deepcopy(a)
#     a_li = [0]*100
#     k=0
#     while a != 0:
#         a_li[k] = a%10
#         a= a//10
#         k +=1

#     a_li = a_li[::-1]
    
#     while a_li[0] == 0:
#         a_li.pop(0)
#     i=0
#     while i < len(a_li)-2:
#         if a_li[i] == 6 and a_li[i+1] == 6 and a_li[i+2] == 6:
#             count+=1
#         i+=1
#     a=a_copy + 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    for i in range(N):
        li = list(map(int,input().split()))
        print(li)