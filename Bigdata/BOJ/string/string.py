from site import setquit
import sys
sys.stdin = open('input.txt','r')

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
# while True:
#     try:
#         n = input()
#         a,b,c,d = 0,0,0,0
#         for i in range(len(n)):
#             if n[i].islower():
#                 a+=1
#             elif n[i].isupper():
#                 b+=1
#             elif n[i].isdigit():
#                 c+=1
#             elif n[i] ==" ":
#                 d+=1
#         print(a,b,c,d)
#     except:
#         break

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

# 2789

# S = input()
# list_S = list(S)
# cambridge= ['C','A','M','B','R','I','D','G','E']
# result =[]
# count = 0

# for i in range(len(S)):
#     if list_S[i] not in cambridge:
#         result.append(list_S[i])
    
# print(''.join(result))

# 2711

# T = int(input())

# for i in range(T):
#     a, b = map(str, input().split())
#     a = int(a)
#     b = list(b)
#     b[a-1] =''
#     print(''.join(b))

# 10102

# V =int(input())
# a =list(input())
# A = 0
# B = 0
# for i in range(V):
#     if a[i] =='A':
#         A +=1
#     elif a[i] =='B':
#         B +=1

# if A > B:
#     print('A')
# elif B > A:
#     print('B')
# else:
#     print('Tie')

# 1919

# A = list(input())
# B = list(input())
# A_count = [0] * 26
# B_count = [0] * 26
# count = 0

# for i in range(len(A)):
#     A_count[ord(A[i])-97] +=1

# for j in range(len(B)):
#     B_count[ord(B[j])-97] +=1

# for i in range(26):
#     if A_count[i] != B_count[i]:
#         count += max([A_count[i],B_count[i]]) - min([A_count[i],B_count[i]])
    
# print(count)

# 1225

# a, b = map(str,input().split())
# a_list = list(a)
# b_list = list(b)
# total = 0

# for i in range(len(a_list)):
#     a_list[i] = int(a_list[i])

# for j in range(len(b_list)):
#     total += sum(a_list) * int(b_list[j])

# print(total)

# 10821

# a= list(map(int,input().split(',')))
# print(len(a))

# 2810

# N = int(input())

# L = list(input())
# if L.count('L') >= 2:
#     count = N - L.count('L') // 2 +1
# else:
#     count = N

# print(count)

# 5218

# T = int(input())

# for i in range(1, T+1):

#     a,b = map(str,input().split())
#     a = list(a)
#     b = list(b)
#     result= []

#     for j in range(len(a)):
#         if ord(b[j]) >= ord(a[j]):
#             result.append(str(ord(b[j])-ord(a[j])))
#         elif ord(a[j]) > ord(b[j]):
#             result.append(str(ord(b[j])-ord(a[j])+26))

#     print(f'Distances: {" ".join(result)}')

# 11098

# n = int(input())

# for i in range(n):
#     p = int(input())
#     dic = {}
#     for j in range(p):
#         a, b = map(str, input().split())
#         dic[int(a)] = b
#     print(dic.get(max(dic)))
    
# 1244

# n = int(input())
# a = list(map(int,input().split()))
# stu_num = int(input())

# for k in range(stu_num):
#     mf, re_num = map(int,input().split())

#     if mf == 1:
#         for i in range(n):
#             if (i+1) % re_num == 0:
#                 if a[i] == 0:
#                     a[i] = 1
#                 elif a[i] == 1:
#                     a[i] = 0
#     else:
#         if a[re_num-1] == 0:
#             a[re_num-1] = 1
#         elif a[re_num-1] == 1:
#             a[re_num-1] = 0
#         j=1

#         while True:
#             if re_num-j >= 1 and re_num+j <= n:
#                 if a[re_num+j-1] == 0 and a[re_num-j-1] == 0:
#                     a[re_num+j-1], a[re_num-j-1] = 1, 1
#                     j +=1
#                     continue
#                 elif a[re_num+j-1] == 1 and a[re_num-j-1] == 1:
#                     a[re_num+j-1], a[re_num-j-1] = 0, 0
#                     j +=1
#                     continue
#                 else:
#                     break
#             else:
#                 break

# for var in a[:-1]:
#     print(var, end=" ")
# print(a[-1])

# 2309
# import random

# h_list = []
# for i in range(9):
#     height = int(input())
#     h_list.append(height)
# while True:
#     ran_li = random.sample(h_list,7)
#     if sum(ran_li) == 100:
#         ran_li.sort()
#         for v in ran_li:
#             print(v)
#             break

# 2477

# n = int(input())
# dic = {}
# lose =[]
# for i in range(6):
#     a,b = map(int,input().split())
#     if str(a) in dic:
#         if b> dic[str(a)]:
#             lose.append([a,dic[str(a)]])
#             dic[str(a)] = b

#         else:
#             lose.append([a,b])
#     dic[str(a)] = b

# print((max(dic['4'],dic['3'])*max(dic['2'],dic['1'])-lose[0][1]*lose[1][1])*n)

# 11656

# S = list(map(str,input()))
# S_list=[]
# for i in range(len(S)-1,-1,-1):
#     s= ",".join(S[i:])
#     s = s.replace(",","")
#     S_list.append(s)
# S_list.sort()
# print(*S_list, sep="\n")


# 3029

# a = input()
# b = input()

# h1 = int(a[:2])
# m1 = int(a[3:5])
# d1 = int(a[6:])

# h2 = int(b[:2])
# m2 = int(b[3:5])
# d2 = int(b[6:])
# if h1 == h2 and m1 == m2 and d1 == d2:
#     print('24:00:00')
# else:
#     h = h2 - h1
#     m = m2 - m1
#     d = d2 - d1

#     if d < 0:
#         d = d + 60
#         m = m - 1
#     if m < 0:
#         m = m + 60
#         h = h - 1
#     if h < 0:
#         h = h + 24

#     if d < 10:
#         d = '0' +str(d)
#     if m < 10:
#         m = '0' +str(m)
#     if h < 10:
#         h = '0' +str(h)

#     print(f'{h}:{m}:{d}')

# 9046
# T = int(input())


# for t in range(T):
#     s= input()
#     s =s.replace(' ','')

#     counts = [0] * 26
    
#     for val in s:
#         counts[ord(val)-97] += 1

#     if counts.count(max(counts)) > 1:
#         print("?")
#     else:
#         print(chr(counts.index(max(counts)) + 97))

# 20154

# num = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

# S = input()
# K = len(S)

# S_num = [0] * (K+1)

# for i in range(K):
#     S_num[i] = num[ord(S[i]) - 65]

# while S_num[1] != 0:
#     for i in range(0,len(S_num),2):
#         try:
#             S_num[i//2] = S_num[i] + S_num[i+1]
#             S_num[i+1] = 0
#         except:
#             pass
#     S_num = S_num[:len(S_num)//2] + [0]

# if S_num[0] % 2 == 1:
#     print("I'm a winner!")
# else:
#     print("You're the winner?")


# 4659

# def good(s):
    
#     collection = ['a','e','i','o','u']
#     count=0
#     for i in range(len(s)):
#         if s[i] in collection:
#             count+=1
    
#     if count > 0:
#         pass
#     else:
#         return 0
            

#     for i in range(len(s)-2):
#         if s[i] in collection and s[i+1] in collection and s[i+2] in collection:
#             return 0
#         elif s[i] not in collection and s[i+1] not in collection and s[i+2] not in collection:
#             return 0
#         else:
#             continue

#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             if s[i] == 'e' and s[i+1] == 'e':
#                 continue
#             elif s[i] == 'o' and s[i+1] == 'o':
#                 continue
#             else:
#                 return 0

#     return 1

# while True:
#     S = input()
#     if S == 'end':
#         break

#     if good(S):
#         print(f'<{S}> is acceptable.')
#     else:
#         print(f'<{S}> is not acceptable.')

# 16171

# S = input()

# K = list(input())

# new = []
# for i in range(len(S)):
#     if S[i].isupper():
#         new.append(S[i])
#     elif S[i].islower():
#         new.append(S[i])
#     else:
#         pass

# s = ''.join(new)
# k = ''.join(K)

# if k in s:
#     print(1)
# else:
#     print(0)

# 6550

# while True:
#     try:
#         s, t = map(str, input().split())

#         S = list(s)
#         T = list(t)

#         new_T = []
#         for val in T:
#             if val in S:
#                 new_T.append(val)

#         ans = 0

#         for i in range(len(new_T)-len(S)+1):
#             if S[0] == new_T[i]:
#                 k = i + 1
#                 j = 1
#                 count = 1
#                 for v in range(len(S)-1):
#                     if S[j] in new_T[k:]:
#                         k = i + new_T[k:].index(S[j]) + 2
#                         j +=1
#                         count +=1
#                     else:
#                         break
#             if count == len(S):
#                 ans = 1
#                 break

#         if ans == 0:
#             print('No')
#         elif ans == 1:
#             print('Yes')

#     except:
#         break

# 9342

# T = int(input())

# for t in range(1,T+1):
#     S = list(input())
#     print(S)
#     count = 0
    
#     if 'A' in S[0:]:
#         count += 1
#     else:
#         print('Good')
#         continue

#     if 'F' in S[S.index('A')+1:]:
#         count += 1
#     else:
#         print('Good')
#         continue
    
#     if 'C' in S[S[S.index('A')+1:].index('F')+1:]:
#         count += 1
#     else:
#         print('Good')
#         continue

#     if len(S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:])==0:
#         pass
#     elif len(S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:])==1:
#         if S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:] in ['A','B','C','D','E','F']:
#             pass
#         else:
#             print('Good')
#             continue
#     else:
#         print('Good')
#         print(count)
#         continue

#     print(count)

# 1764

# N, M = map(int, input().split())

# N_list = [' '] * N
# M_list = [' '] * M

# for n in range(N):
#     N_name = input()
#     N_list[n] = N_name

# for m in range(M):
#     M_name = input()
#     M_list.append(M_name)


# NM_list = set(N_list) & set(M_list)
# NM_list = list(NM_list)
# NM_list.sort()

# print(len(NM_list))
# for val in NM_list:
#     print(val)

# 20291

# N = int(input())

# dic = {}

# for _ in range(N):
#     S = input()
#     exten = S[S.find('.')+1:] #확장자
    
#     if exten not in dic:
#         dic[exten] = 1
#     elif exten in dic:
#         dic[exten] += 1

# sorted_dic = sorted(dic.items())

# for i in range(len(sorted_dic)):
#     print(*sorted_dic[i])

# 17413

# S = list(input())

# new_S = []
# stk = []

# for i in range(len(S)):
#     if S[i] == '<':
#         idx_s = i
#         stk.append('<')
#     elif S[i] == '>':
#         idx_e = i
#         stk.pop(-1)
#         new_S.append(''.join(S[idx_s:idx_e+1]))
    
# print(new_S)