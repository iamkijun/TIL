import sys
sys.stdin = open("input.txt","r")

# 10817

# A = list(map(int,input().split()))
# A.sort()

# print(A[1])

# 2440

# N = int(input())

# for i in range(N,0,-1):
#     print("*"*i)

#  2775

# T = int(input())
# sum = 0
# for i in range(T):
#     k=int(input())
#     n=int(input())
#     for k in range(1,b):
#         sum += k
#     print(sum)

# 2441
# N = int(input())

# for i in range(N):
#     print(" "*i + "*"*(N-i))

# 2442
# N = int(input())

# for i in range(1,N+1):
#     print(" "*(N-i) + "*"*(2*i-1))


# 2443
# N = int(input())

# for i in range(N,0,-1):
#     print(" "*(N-i) + "*"*(2*i-1))

# 2444
# N = int(input())

# for i in range(1,N+1):
#     print(" "*(N-i) + "*"*(2*i-1))
# for j in range(N-1,0,-1):
#     print(" "*(N-j) + "*"*(2*j-1))

# 2445
# N = int(input())

# for i in range(1,N+1):
#     print("*"*i+ " "*(2*(N-i))+ "*"*i)
# for j in range(N-1,0,-1):
#     print("*"*j+ " "*(2*(N-j))+ "*"*j)

# 2446
# N = int(input())

# for i in range(0,N):
#     print(" "*i+"*"*(2*(N-i)-1))
# for j in range(N-1,0,-1):
#     print(" "*(j-1)+"*"*(2*(N-j)+1))

# 2522

# N = int(input())

# for i in range(1,N+1):
#     print(" "*(N-i) + "*"*i)
# for j in range(N-1,0,-1):
#     print(" "*(N-j) + "*"*j)

# 2523

# N = int(input())

# for i in range(1,N+1):
#     print("*"*i)
# for j in range(1,N):
#     print("*"*(N-j))


# 10990

# N = int(input())
# print(" "*(N-1)+"*")
# for i in range(2,N+1):
#     print(" "*(N-i)+"*"+" "*(2*i-3) +"*")

# 10991

# N = int(input())
# for i in range(0,N+1):
#     if i != 0:
#         print(" "*(N-i), end="")
#     for j in range(0,i-1):
#         print("*", end=" ")
#     if i !=0:
#         print("*")


# 10992

# N = int(input())
# if N != 1:
#     print(" "*(N-1)+"*")
# for i in range(N-2):
#     print(" "*(N-i-2) +"*"+" "*(2*i+1)+"*")
# print("*"*(2*N-1))

# 10995

# N = int(input())

# for i in range(N):
#     for j in range(N):
#         if i % 2==1:
#             print(" "+"*", end="")
#         elif i % 2 == 0:
#             print("*"+" ", end="")
#     print("")

# 10996

# N = int(input())
# if N % 2 == 0:
#     for i in range(N):
#         print("* " * (N//2))
#         print(" *"* (N//2))
# elif N % 2 == 1:
#     for i in range(N):
#         print("* "*(N//2+1))
#         print(" *"*(N//2))

# 9291

# T = int(input())

# for t in range(1,T+1):

#     arr = [list(map(int,input().split())) for _ in range(9)]

#     num_li = [1,2,3,4,5,6,7,8,9]
    
#     count = 0

#     for i in range(9):
#         stack_num_h = []
#         stack_num_v = []

#         for j in range(9):
            
#             stack_num_h.append(arr[i][j])
#             stack_num_v.append(arr[j][i])
        
#         if set(stack_num_h) != set(num_li):
#             count += 1
#         if set(stack_num_v) != set(num_li):
#             count += 1

#     for i in range(3):
#         stack_num_box = []
#         for j in range(3):
#             for k in range(3):
#                 stack_num_box.append(arr[i*3+j][i*3+k])
#         if set(stack_num_box) != set(num_li):
#             count += 1

#     if count > 0:
#         print(f'Case {t}: INCORRECT')
#     else:
#         print(f'Case {t}: CORRECT')

#     N = sys.stdin.readline()