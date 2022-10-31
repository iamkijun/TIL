import sys
input = sys.stdin.readline

# 2750
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))

# l.sort()

# for i in range(n):
#     print(l[i])


# 11650

# N = int(input())
# l =[]
# for _ in range(N):
#     a = list(map(int,input().split()))
#     l.append(a)

# l.sort(key = lambda x: (x[0],x[1]))

# for i in range(N):
#     print(l[i][0], l[i][1])

# 11651

# N = int(input())
# l = []

# for _ in range(N):
#     a = list(map(int,input().split()))
#     l.append(a)

# l.sort(key = lambda x: (x[1],x[0]))

# for i in range(N):
#     print(l[i][0], l[i][1])

# 1427
# N = list(input())

# for i in range(len(N)):
#     N[i] = int(N[i])

# N.sort(reverse = True)

# for i in range(len(N)):
#     N[i] = str(N[i])

# print("".join(N))

# 1181

# N = int(input())
# l = []

# for i in range(N):
#     a = input()
#     l.append(a)

# l = set(l)
# l = list(l)

# l = sorted(l, key = lambda x: (len(x),x))

# for j in range(len(l)):
#     print(l[j])

#  10814 - 시간초과
# import sys
# N = int(sys.stdin.readline())
# l = []
# for i in range(N):
#     a = list(map(str, sys.stdin.readline().split()))
#     l.append(a)

# l = sorted(l, key = lambda x: (x[0], l.index(x[:])))

# for i in range(N):
#     print(l[i][0], l[i][1])
# for x in l:
#     print(x[0], x[1])

# # 18870
# import sys 
# N = int(sys.stdin.readline())

# a = list(map(int, sys.stdin.readline().split()))

# l = []

# b = set(a)
# b = list(b)

# for i in range(N):
#     count = 0
#     for j in range(len(b)):
#         if a[i] > b[j]:
#             count+=1
    
#     print(count, end=" ")

# 2751
# import sys

# n = int(sys.stdin.readline())
# l = []
# for i in range(n):
#     l.append(int(sys.stdin.readline()))

# l.sort()

# for i in range(n):
#     print(l[i])

# N = int(input())

# li = list(map(int, input().split()))
# li.sort()
# real_total = li[0]
# total =  li[0]

# for i in range(1,N):
#     total = total + li[i]
#     real_total += total
# print(real_total)

#10989
# import sys

# n = int(sys.stdin.readline())
# l = [0] * 10001
# for i in range(n):
#     l.append(int(sys.stdin.readline()))

# l.sort()

# for num in l:
#     print(num)

# 10814

# import sys
# N = int(sys.stdin.readline())
# l = []
# for i in range(N):
#     a = list(map(str, sys.stdin.readline().split()))
#     l.append(a)

# l = sorted(l, key = lambda x: (x[0], l.index(x[:])))

# for i in range(N):
#     print(l[i][0], l[i][1])

# 2693

# T= int(input())

# for _ in range(T):
    
#     N= int(input())
#     arr =[]
#     maxV = 0
#     for i in range(N):
#         li = list(map(str, input().split()))
#         li[1]= int(li[1])
#         arr.append(li)
#         if arr[i][1] > maxV:
#             maxV = arr[i][1]
#             school_name = arr[i][0]
        
#     print(school_name)

# 5576

# w_li =[]
# k_li =[]
# for i in range(10):
#     w = int(input())
#     w_li.append(w)

# for j in range(10):
#     k = int(input())
#     k_li.append(k)

# w_li.sort(reverse=True)
# k_li.sort(reverse=True)
# print(sum(w_li[:3]), sum(k_li[:3]))

# 1026

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# B.sort()
# A.sort(reverse=True)

# result = 0
# for i in range(N):
#     result += A[i] * B[i]
# print(result)

# 2766

# T= int(input())

# for t in range(T):
#     N = int(input())
#     N_list = list(map(int,input().split()))
#     M = int(input())
#     M_list = list(map(int,input().split()))

#     for m in M_list:
#         if m in N_list:
#             print(1)
#         else:
#             print(0)

# 5800

# X = int(input())
# for x in range(1,X+1):
#     x_list = list(map(int, input().split()))
#     N = x_list[0]
#     x_list = x_list[1:]

#     print(f'Class {x}')
    
#     max_dif = 0

#     for i in range(N-1):
#         maxIdx = i
#         for j in range(i,N):
#             if x_list[maxIdx] < x_list[j]:
#                 maxIdx = j
#         x_list[maxIdx], x_list[i] = x_list[i], x_list[maxIdx]
        
#         if i >=1:
#             dif = x_list[i-1]- x_list[i]
#             if dif > max_dif:
#                 max_dif = dif
#     dif = x_list[-2]- x_list[-1]
#     if dif > max_dif:
#         max_dif = dif
#     print(f'Max {x_list[0]}, Min {x_list[-1]}, Largest gap {max_dif}')

# 1940 시간초과

# N = int(input())
# M = int(input())

# N_list = list(map(int, input().split()))
# count = 0

# for i in range(N-1):
#     for j in range(i,N):
#         if N_list[i] + N_list[j] == M:
#             count +=1

# print(count)

# 11004

N , K = map(int, input().split())
N_list = list(map(int, input().split()))

for i in range(N-1):
    for j in range(i,N):
        if N_list[i]< N_list[j]