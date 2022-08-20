# #15596
# def solve(a):
#     ans = 0
#     for i in range(len(a)):
#         ans += a[i]
#     return ans

# #1065
# def solve(a):
#     count = 0
#     for i in range(1,a+1):
#         if i >= 1 and i <10:
#             count +=1
            
#         elif i >= 10 and i <100:
#                 count +=1

#         elif i >= 100 and i <1000:
#             thr = i // 100
#             sec = (i // 10) % 10
#             fir = i % 10
            
#             if fir == sec == thr:
#                 count+=1

#             if thr == sec:
#                 continue
#             elif thr == fir:
#                 continue
#             elif sec == fir:
#                 continue

            
            
#             if abs(thr - sec) == abs(sec - fir):
#                 count += 1
            
#         elif i == 1000:
#             pass
        
        
        
        
#     return count

# n = int(input())

# print(solve(n))

# #4673 진행중
for i in range(1,10001):
    if i == 10000:
        
    elif i >= 1000:

    elif i>= 100:

    elif i>= 10:

    else: