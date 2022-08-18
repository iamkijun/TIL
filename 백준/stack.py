from pydoc_data.topics import topics
import sys
sys.stdin = open("input.txt","r")

# 9012
# T = int(input())

# for t in range(1,T+1):
    
#     S = input()

#     stk = []
#     ans = 1

#     for val in S:
#         if val == '(':
#             stk.append('(')
#         elif val == ')':
#             if stk:
#                 stk.pop(-1)
#             else:
#                 ans = 0
#                 break
#     else:
#         if len(stk) != 0:
#             ans =0

#     if ans:
#         print('YES')
#     else:
#         print('NO')

# 10828

# N = int(sys.stdin.readline())

# stk = []

# for i in range(N):
    
#     arr = list(map(str, sys.stdin.readline().split()))
    
#     if arr[0] == 'push':
#         stk.append(arr[1])

#     elif arr[0] == 'pop':
#         if len(stk) > 0:
#             print(stk[-1])
#             stk.pop(-1)
#         elif len(stk) == 0:
#             print(-1)

#     elif arr[0] == 'size':
#         print(len(stk))

#     elif arr[0] == 'empty':
#         if stk == []:
#             print(1)
#         else:
#             print(0)

#     elif arr[0] == 'top':
#         if len(stk) > 0:
#             print(stk[-1])
#         elif len(stk) == 0:
#             print(-1)

# 10773

# K = int(input())

# stk = []

# for i in range(K):
#     n = int(input())

#     if n == 0:
#         stk.pop(-1)
#     else:
#         stk.append(n)

# print(sum(stk))


# 4949

# while True:
#     S = input()

#     if S == '.':
#         break
#     else:
#         ans = 1

#         stk = []

#         for val in S:
#             if val == '(':
#                 stk.append('(')
            
#             elif val == '[':
#                 stk.append('[')
            
#             elif val == ')':
#                 if stk and stk[-1] == '(':
#                     stk.pop(-1)
#                 else:
#                     ans = 0
#                     break
            
#             elif val == ']':
#                 if stk and stk[-1] == '[':
#                     stk.pop(-1)
#                 else:
#                     ans = 0
#                     break
        
#         if stk != []:
#             ans= 0
        
#     if ans:
#         print('yes')
#     else:
#         print('no')

# 1874

# n = int(input())

# stk = []

# for i in range(n):
#     num = int(input())
#     stk.append(num)

# print(stk)

# 12605

# T = int(input())

# for t in range(1,T+1):

#     li = list(map(str, input().split()))

#     print(f'Case #{t}:',*li[::-1])