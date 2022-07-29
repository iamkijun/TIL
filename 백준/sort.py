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
import sys
N = int(sys.stdin.readline())
l = []
for i in range(N):
    a = list(map(str, sys.stdin.readline().split()))
    l.append(a)

l = sorted(l, key = lambda x: (x[0], l.index(x[:])))

for i in range(N):
    print(l[i][0], l[i][1])
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

