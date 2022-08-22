#  3009

# a,b = map(int, input().split())
# c,d = map(int, input().split())
# e,f = map(int, input().split())

# if a == c:
#     print(e, end=" ")
# elif a == e :
#     print(c, end=" ")
# elif e == c:
#     print(a, end=" ")

# if b == d:
#     print(f)
# elif b == f:
#     print(d)
# elif f == d:
#     print(b)

#  4153

# while True:
#     a = list(map(int, input().split()))

#     if a == [0,0,0]:
#         break
#     else:
#         a.sort()
#         if a[0]**2 + a[1]**2 == a[2]**2:
#             print("right")
#         else:
#             print("wrong")

# 1085

# a,b,c,d = map(int, input().split())

# min = 1000

# if a < min:
#     min = a
# if (c - a) < min:
#     min = c - a
# if b < min:
#     min = b
# if (d - b) < min:
#     min = d - b

# print(min)

# 2477 답은 맞는데 계속 틀림


# n = int(input())
# a_list = [] #방향 리스트
# b_list = [] #거리 리스트

# a_num = [0,0,0,0] # 방향 횟수 리스트

# for i in range(6):
#     a,b = map(int,input().split())

#     a_list.append(a)
#     if a == 1:
#         a_num[0] += 1
#     elif a == 2:
#         a_num[1] += 1
#     elif a == 3:
#         a_num[2] += 1
#     elif a == 4:
#         a_num[3] += 1
    
#     b_list.append(b)

# k = []
# s = []
# for i in range(4):
#     if a_num[i] == 1:
#         k.append(b_list[a_list.index(i+1)])
#     if a_num[i] == 2:
#         s.append(a_list[a_list.index(i+1)])


# rest_list1 = list(filter(lambda x: a_list[x] == s[0], range(len(a_list))))
# rest_list2 = list(filter(lambda x: a_list[x] == s[1], range(len(a_list))))
# print(rest_list1, rest_list2)
# if rest_list1[0]>rest_list2[0]:
#     small_area = b_list[rest_list1[0]] * b_list[rest_list2[1]]
# elif rest_list2[0]>rest_list1[0]:    
#         small_area = b_list[rest_list1[1]] * b_list[rest_list2[0]]
# area = k[0] * k[1] - small_area
# print(area * n)

# 3053

# import math
# num = int(input())

# print(f'{(num**2) * math.pi :.6f}')
# print(f'{(num**2) * 2 :.6f}')

# 1358 제대로 짠 것 같은데 틀리게 나옴

# W, H, X, Y, P = map(int, input().split())
# count = 0
# for i in range(P):
#     x, y =map(int,input().split())
#     if abs(x-X)**2 + abs(y -Y+H/2)**2 <= (H/2)**2:
#         count+=1
#     elif abs(x-X+W)**2 + abs(y -Y+H/2)**2 <= (H/2)**2:
#         count+=1
#     elif x >= X and x <= X-W and y >= Y and y <= Y-H:
#         count+=1

# print(count)