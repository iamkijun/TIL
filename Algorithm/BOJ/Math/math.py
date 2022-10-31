#5086

# while True:
#     a, b= map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     else:
#         if a % b == 0:
#             print("multiple")
#         elif b % a == 0:
#             print("factor")
#         else:
#             print("neither")


# 1037 맞는 것 같은데 아님...

# n = int(input())
# a = list(map(int,input().split()))

# start = max(a) -1

# while True:
#     start += 1
#     for i in range(len(a)):
#         if start % a[i] == 0:
#             pass
#         else:
#             continue
#     print(start * 2)
#     break
    
# 2609 시간초과

# a, b =map(int, input().split())

# x, y = min(a,b), max(a,b)

# while True:
#     if a % x ==0 and b % x ==0:
#         break
#     else:
#         x -= 1

# while True:
#     if y % a == 0 and y % b == 0:
#         break
#     else:
#         y += 1
        
# print(x)
# print(y)

# 1934 

# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())

#     print()