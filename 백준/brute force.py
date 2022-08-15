import sys
sys.stdin = open("input.txt","r")


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

# 1075

# N = int(input())
# F = int(input())

# minV = 100

# N = (N // 100) * 100

# for i in range(100):
#     val = (N+i) % F 
#     if val == 0:
#         if i < minV:
#             minV = i
# if minV < 10:
#     minV = '0' + str(minV)
# print(minV)

# 3040

# num_li = []

# for _ in range(9):
#     n = int(input())
#     num_li.append(n)

# for i in range(1<<9):
#     count = 0
#     total = []
#     for j in range(i):
#         if i & (1<<j):
#             total.append(num_li[j])
#             count+=1
#     if count == 7 and sum(total) == 100:
#         break

# for j in range(7):
#     print(total[j])

# 10448

# T = int(input())

# def ureca(a):
#     i = 2
#     li = [1,]
#     while li[-1]<=a:
#         val = i*(i+1)//2
#         li.append(val)
#         i +=1
    
#     return li

# for t in range(1,T+1):
#     N = int(input())

#     a = ureca(N)
#     l = len(a)

#     count = 0
    
#     for i in range(l):
#         for j in range(l):
#             for k in range(l):=
#                 if a[i] + a[j] + a[k] == N:
#                     count +=1
#                     break
#             if count >0:
#                 break
#         if count>0:
#             break

                    
#     if count > 0:
#         print(1,count)
#     else:
#         print(0)

# 2851

# li = []

# for _ in range(10):
#     n= int(input())
#     li.append(n)

# total = 0
# for i in range(10):
#     total += li[i]
#     if total >= 100:
#         if abs(100 -(total - li[i])) < abs(100 -total):
#             print(total - li[i])
#         else:
#             print(total)
#         break

# if sum(li) < 100:
#     print(sum(li))

# 2702

# T = int(input())

# for t in range(1,T+1):
#     a, b = map(int,input().split())
    
#     small = 1
    
#     for i in range(min([a,b]),0,-1):
#         if a % i == 0 and b % i == 0:
#             small = i
#             break

#     big = small * (a // small) * (b // small)

#     print(big, small)

# 2670

N = int(sys.stdin.readline())
n_list = []
for t in range(N):
    n = float(sys.stdin.readline())
    n_list.append(n)

maxV = 0
to_li = []
for i in range(N-1):
    totalV = 1
    for j in range(i,N):
        totalV = totalV * n_list[j]
        to_li.append(totalV)
    if max(to_li) > maxV:
        maxV = max(to_li)

print(round(maxV,3))