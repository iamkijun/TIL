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