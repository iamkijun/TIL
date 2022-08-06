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

# # 2941 (왜 안되는지 모르겠음,런타임에러)

# N = input()

# cro_alpha = ['c=','c-','d-','lj','nj','s=','z=']
# a= []
# if len(N) >2:
#     for i in range(0,len(N)-2):
#         if N[i]+N[i+1]+N[i+2] == "dz=":
#             continue
#         elif N[i]+N[i+1] in cro_alpha:
#             continue
#         else:
#             a.append('k')
#     if N[-2]+N[-1] in cro_alpha:
#         a.append('k')
#     else:
#         a.append('k')
#         a.append('k')
# elif len(N) ==2:
#     if N[-2]+N[-1] in cro_alpha:
#         a.append('k')
#     else:
#         a.append('k')
#         a.append('k')
# elif len(N) ==1:
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

# # 10820 멈추는 법을 모르겠음
# N= 4
# for i in range(N):
#     n = input()
#     a,b,c,d = 0,0,0,0
#     for i in range(len(n)):
#         if n[i].islower():
#             a+=1
#         elif n[i].isupper():
#             b+=1
#         elif n[i].isdigit():
#             c+=1
#         elif n[i] ==" ":
#             d+=1
#     print(a,b,c,d)

# # 1373  시간초과
# n = int(input())
# new = ""
# num = 0

# while True:
#     if n == 0:
#         break
#     else:
#         if n % 1000 >= 100:
#             num +=4
#         if n % 100 >= 10:
#             num +=2
#         if n % 10 ==1:
#             num +=1
    

#     new = str(num) + new

#     n = n//1000

#     num = 0

# print(new)        

# 7567

# S = input()
# n = 10
# for i in range(1,len(S)):
#     if S[i-1]==S[i]:
#         n +=5
#     elif S[i-1]!=S[i]:
#         n +=10
# print(n)

# 15829 부분성공

# L = int(input())
# s = input()
# total = 0

# for i in range(L):
#     total += (ord(s[i])%96) * (31 ** i)
# print(total)

# 2744

# s = input()
# new = ""
# for i in range(len(s)):
#     if s[i].isupper():
#         new += s[i].lower()
#     elif s[i].islower():
#         new += s[i].upper()

# print(new)

#2754

# grade = input()
# total = 0

# if grade[0] == 'A':
#     total += 4
# elif grade[0] == 'B':
#     total += 3
# elif grade[0] == 'C':
#     total += 2
# elif grade[0] == 'D':
#     total += 1
# elif grade[0] == 'F':
#     total = 0

# if grade[1] == '+':
#     total += 0.3
# elif grade[1] == '-':
#     total -= 0.3
# else:
#     pass

# print(f'{total:.1f}')

# 1357

# from tkinter import N

# x, y = map(int, input().split())
# def rev(num):
#     new = ""
#     while True:
#         if num == 0:
#             break
#         else:
#             new = new + str(num % 10)

#         num = num // 10
    
#     return int(new)

# print(rev(rev(x) + rev(y)))

# 14425

# N, M = map(int, input().split())
# N_list=[]
# M_list=[]
# count = 0
# for i in range(N):
#     n = input()
#     N_list.append(n)

# N_list = set(N_list)

# for j in range(M):
#     m = input()
#     if m in N_list:
#         count+=1

# print(count)

#  2745

# N, B = map(str, input().split())

# B = int(B)

# count = 0

# for i in range(len(N)):
#     if N[len(N)-i-1].isdigit():
#         count += int(N[len(N)-i-1])*(B**i)
#     elif N[len(N)-i-1].isupper():
#         count += (ord(N[len(N)-i-1])-55)* (B**i)
        

# print(count)

# 1302

# N = int(input())
# book_list = []
# for i in range(N):
#     book = input()
#     book_list.append(book)

# book_set = set(book_list)
# book_set_list = list(book_set)
# book_set_list.sort()

# book_set_count = []
# for i in range(len(book_set_list)):
#     book_set_count.append(book_list.count(book_set_list[i]))

# print(book_set_list[book_set_count.index(max(book_set_count))])

# # 1120

# A, B = map(str, input().split())
# count = 0
# counts =[]
# if len(A) == len(B):
#     for i in range(len(A)):
#         if A[i] != B[i]:
#             count +=1
#     print(count)

# elif len(A) > len(B):
#     for i in range(len(A)-len(B)+1):
#         for j in range(len(B)):
#             if A[i+j] != B[j]:
#                 count += 1
#         counts.append(count)
#         count = 0

#     print(min(counts))

# elif len(B) > len(A):
#     for i in range(len(B)-len(A)+1):
#         for j in range(len(A)):
#             if A[j] != B[i+j]:
#                 count += 1
#         counts.append(count)
#         count = 0

#     print(min(counts))

# 2935

# A = int(input())
# B = input()
# C = int(input())

# if B =="+":
#     print(A+C)
# elif B == "*":
#     print(A*C)

# 1159

# N = int(input())
# li=[]
# for i in range(N):
#     name = input()
#     li.append(name)

# first_name=[]
# alpha_list=[0]*26
# for j in range(N):
#     alpha_list[(ord(li[j][0])-97)] +=1

#     if alpha_list[(ord(li[j][0])-97)] == 5:
#         first_name.append(li[j][0])


# if first_name ==[]:
#     print("PREDAJA")
# else:
#     first_name.sort()
#     print(''.join(first_name))

#  11365
# s=''
# while True:
#     s = input()
#     if s =='END':
#         break
#     print(s[::-1])

# 10987
# s = input()
# li = ['a','e','i','o','u']
# count = 0
# for i in range(len(s)):
#     if s[i] in li:
#         count+=1

# print(count)

# 5598
# S = input()

# for i in range(len(S)):
#     if i==len(S)-1:
#         if ord(S[i]) >= 68:
#             print(chr(ord(S[i])-3))
#         elif ord(S[i]) <= 67:
#             print(chr(ord(S[i])+23))
#     else:
#         if ord(S[i]) >= 68:
#             print(chr(ord(S[i])-3),end="")
#         elif ord(S[i]) <= 67:
#             print(chr(ord(S[i])+23),end="")

# 1652
# hor = 0
# ver = 0
# li = []
# N = int(input())

# for i in range(N):
#     a = input()
#     a = list(a)
#     li.append(a)

# for i in range(N):
#     for j in range(N-1):
#         if li[j][i] =='.' and li[j+1][i] == '.':
#             hor += 1
#             try:
#                 if li[j+1][i] =='.' and li[j+2][i] == '.':
#                     hor -=1
#             except:
#                 pass
            
#         if li[i][j] =='.' and li[i][j+1] == '.':
#             ver += 1
#             try:
#                 if li[i][j+1] =='.' and li[i][j+2] == '.':
#                     ver -=1
#             except:
#                 pass
            
            
# print(ver, hor)

# 5635
# n = int(input())

# info_list = []
# for i in range(n):
#     ndmy = list(map(str, input().split()))
#     ndmy[1], ndmy[2], ndmy[3] = int(ndmy[1]), int(ndmy[2]), int(ndmy[3])
#     info_list.append(ndmy)
# oldy = info_list[0][3]
# oldm = info_list[0][2]
# oldd = info_list[0][1]
# remember_old = info_list[0][0]
# youngy = info_list[0][3]
# youngm = info_list[0][2]
# youngd = info_list[0][1]
# remember_young = info_list[0][0]

# for i in range(1,n):
#     if info_list[i][3] > youngy:
#         youngy = info_list[i][3]
#         youngm = info_list[i][2]
#         youngd = info_list[i][1]
#         remember_young = info_list[i][0]
#     elif info_list[i][3] == youngy:
#         if info_list[i][2] > youngm:
#             youngy = info_list[i][3]
#             youngm = info_list[i][2]
#             youngd = info_list[i][1]
#             remember_young = info_list[i][0]
#         elif info_list[i][2] == youngm:
#             if info_list[i][1] > youngd:
#                 youngy = info_list[i][3]
#                 youngm = info_list[i][2]
#                 youngd = info_list[i][1]
#                 remember_young = info_list[i][0]

#     if info_list[i][3] < oldy:
#         oldy = info_list[i][3]
#         oldm = info_list[i][2]
#         oldd = info_list[i][1]
#         remember_old = info_list[i][0]
#     elif info_list[i][3] == oldy:
#         if info_list[i][2] < oldm:
#             oldy = info_list[i][3]
#             oldm = info_list[i][2]
#             oldd = info_list[i][1] 
#             remember_old = info_list[i][0]
#         elif info_list[i][2] == oldm:
#             if info_list[i][1] < oldd:
#                 oldy = info_list[i][3]
#                 oldm = info_list[i][2]
#                 oldd = info_list[i][1]
#                 remember_old = info_list[i][0]
    
# print(remember_young)
# print(remember_old)

# 10769

# S = input()
# count_smile= S.count(':-)')
# count_sad= S.count(':-(')

# if count_smile + count_sad == 0:
#     print('none')
# elif count_smile > count_sad:
#     print('happy')
# elif count_smile < count_sad:
#     print('sad')
# elif count_smile == count_sad:
#     print('unsure')

