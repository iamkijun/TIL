# #11654
# N = input()

# print(ord(N))

# 11720
#  N = int(input())

# a = input()
# sum = 0
# for i in range(N):
#     sum += int(a[i])

# print(sum)

# 10809
# S = input()

# alpha = []
# l = [-1] * 26

# for k in range(97,123):
#     alpha.append(chr(k))


# for i in range(len(S)):
#     if l[alpha.index(S[i])] == -1:
#         l[alpha.index(S[i])] = i

# for j in range(26):
#     print(l[j], end=" ")

#  2675

# T = int(input())
# for i in range(T):
#     a, b = map(str, input().split())
#     for j in range(len(b)):
#         print(b[j]*int(a), end='')
#     print('')

#  1157

# n = input()
# n = n.upper()

# l =[]
# l_num = [0] * 26
# for i in range(65,91):
#     l.append(chr(i))

# for j in range(len(n)):
#     l_num[l.index(n[j])] +=1

# if l_num.count(max(l_num)) >= 2:
#     print('?')
# else:
#     print(l[l_num.index(max(l_num))])

#  1152

# n = input().split()
# print(len(n))

#  2908

# a, b = map(int,input().split())

# c = a//100+ ((a//10)%10)* 10 + (a%10)*100
# d = b//100+ ((b//10)%10)* 10 + (b%10)*100

# if c>d:
#     print(c)
# elif d>c:
#     print(d)

# 5622

# n = input()
# sum = 0
# for i in range(len(n)):
#     if n[i] == 'A' or n[i] =='B' or n[i] =='C':
#         sum+=3
#     elif n[i] == 'D' or n[i] =='E' or n[i] =='F':
#         sum+=4
#     elif n[i] == 'G' or n[i] =='H' or n[i] =='I':
#         sum+=5
#     elif n[i] == 'J' or n[i] =='K' or n[i] =='L':
#         sum+=6
#     elif n[i] == 'M' or n[i] =='N' or n[i] =='O':
#         sum+=7
#     elif n[i] == 'P' or n[i] =='Q' or n[i] =='R' or n[i] =='S':
#         sum+=8
#     elif n[i] == 'T' or n[i] =='U' or n[i] =='V':
#         sum+=9
#     elif n[i] == 'W' or n[i] =='X' or n[i] =='Y' or n[i] =='Z':
#         sum+=10

# print(sum)

# 2941 (왜 안되는지 모르겠음,런타임에러)

# N = input()

# cro_alpha = ['c=','c-','d-','lj','nj','s=','z=']
# a= []
# for i in range(0,len(N)-2):
#     if N[i]+N[i+1]+N[i+2] == "dz=":
#         continue
#     elif N[i]+N[i+1] in cro_alpha:
#         continue
#     else:
#         a.append('k')

# if N[-2]+N[-1] in cro_alpha:
#     a.append('k')
# else:
#     a.append('k')
#     a.append('k')

# print(len(a))

#  1316

# N = int(input())
# total = 0


# for i in range(N):
#     li = []
#     a=0
#     s = list(input())

#     for j in range(len(s)):
#         if s[j] not in li:
#             li.append(s[j])
#         elif s[j] in li:
#             if s[j-1] == s[j]:
#                 pass
#             elif s[j-1] != s[j]:
#                 a=1
#     if a == 0:
#         total += 1
        
# print(total)

#  1712

# A, B, C = map(int, input().split())

# if (C-B) == 0:
#     print(-1)

# elif A // (C-B) < 0:
#     print(-1)

# else:
#     print(A // (C-B) + 1)

#  2292 대충 알겠는데 코드로 못짜겟음

# n = int(input)

# count = 0

# 2 7//8  19//20 37///38 61

# a = n//6 +1

# 1193 너무 어려움

# n = int(input())

# print(n % int(n**0.5))

# print(n// int(n**0.5))

# 2869 알것 같은데 어려움

# A, B, C = map(int, input().split())

# day = C // (A-B) 

# if (A-B)*(day-1) + A >= C:
#     day = day -
# print(day)

# 11721

# n = input()

# while True:
#     if len(n)>10:
#         print(n[:10])
#         n = n[10:]
#     else:
#         print(n)
#         break

#  10953

# T = int(input())

# for i in range(T):
#     a,b=map(int,input().split(","))
#     print(a+b)

# 10808

# alphabet = [0] * 26

# n = input()

# for a in n:
#     for j in range(97,123):
#         if a == chr(j):
#             alphabet[j-97] +=1

# result = ' '.join(str(s) for s in alphabet)
# print(result)

# 1259

# while True:
#     n =input()
#     if n=='0':
#         break
#     elif n == n[::-1]:
#         print('yes')
#     else:
#         print('no')
    
# 1100

# total = []
# li =[]
# count =0
# for i in range(8):
#     a=str(input())
#     for j in range(8):
#         li.append(a[j])
#     total.append(li)
#     li = []

# for i in range(8):
#     for j in range(8):
#         if i % 2 ==0 and j % 2 ==0:
#             if total[i][j] =='F':
#                 count +=1
                
#         if i % 2 == 1 and j % 2 ==1:
#             if total[i][j] =='F':
#                 count +=1
                

# print(count)

# 1032 

# N = int(input())
# l = []
# for i in range(N):
#     f = input()
#     l.append(f)

# first = list(max(l))

# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if first[j] == l[i][j]:
#             pass
#         elif first[j] != l[i][j]:
#             first[j] = '?'

# print(''.join(first))

# 2902

# n = input()
# l = []
# for i in range(len(n)):
#     if n[i].isupper():
#         l.append(n[i])

# print(''.join(l))

# 10988

# n= list(input())

# if n == n[::-1]:
#     print("1")
# else:
#     print("0")

# 1212 왜 안되는지 모르겠음

# n = int(input())
# sum = ''
# while True:
#     if n ==0:
#         break
#     a = int(n) % 10
#     if a % 2 == 0:
#         sum = "0" +sum
#     elif a % 2 == 1:
#         sum = "1" + sum

#     if a // 4 == 0 and a // 2 == 1:
#         sum = "1" +sum
#     else:
#         sum = "0" +sum
    
#     if a //4 ==1:
#         sum = "1" +sum
#     else:
#         sum = "0" +sum

     
    
#     n = n//10
# print(int(sum))

# 9093

# T = int(input())

# for i in range(T):
#     s = list(map(str, input().split()))
#     for i in range(len(s)):
#         s[i] = s[i][::-1]
#     print(" ".join(s))

# 11655

# s = input()
# for i in range(len(s)):
    
#     if s[i].islower():
#         if ord(s[i]) > 109:
#             print(chr(ord(s[i])-13), end="")
#         else:
#             print(chr(ord(s[i])+13), end="")
#     elif s[i].isupper():
#         if ord(s[i]) > 77:
#             print(chr(ord(s[i])-13), end="")
#         else:
#             print(chr(ord(s[i])+13), end="")
#     else:
#         print(s[i], end="")

# 10798
# l=[]
# max_len = 0
# for i in range(5):
#     a = input()
#     l.append(a)
#     if len(a) > max_len:
#         max_len = len(a)

# for i in range(max_len):
#     for j in range(5):
#         try:
#             print(l[j][i], end="")
#         except:
#             pass

# https://flukeout.github.io/

