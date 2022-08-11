# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for t in range(1,T+1):
#
#     K, N, M = map(int,input().split())
#     #K: 한번 충전 이동, N: 총 정류장 수, M: 충전기가 설치된 정류장
#
#     M_li = list(map(int, input().split()))
#
#     count = 0 # 충전 횟수
#     energy = K # 초기 충전
#
#     for i in range(N+1):
#         if i in M_li:
#             if M_li.index(i) != len(M_li)-1: # 마지막 충전소가 아닐 경우,
#                 if energy >= M_li[M_li.index(i)+1]-M_li[M_li.index(i)]:
#                     pass # 다음 충전소까지 에너지가 충분하면 충전안해두됨
#                 elif M_li[M_li.index(i)+1]-M_li[M_li.index(i)]> K:
#                     count = 0 # 충전해도 다음 충전소까지 못가는 경우
#                     break
#                 elif energy < M_li[M_li.index(i)+1]-M_li[M_li.index(i)]:
#                     count+=1 # 충전해서 다음 충전소까지 가기
#                     energy=K
#             elif M_li.index(i) == len(M_li)-1: #마지막 충전소일 경우,
#                 if energy >= N-i: #에너지가 충분하면 지나가
#                     pass
#                 elif energy < N-i: #에너지가 부족하면 충전해서 가기
#                     count+=1
#                     energy=K
#                 elif N-i > K: #에너지를 충전해도 못가는 경우
#                     count= 0
#                     break
#         energy -= 1
#
#     print(f'#{t} {count}')

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for t in range(1,T+1):
#
#     K, N, M = map(int,input().split())
#
#     M_li = list(map(int, input().split()))
#
#     count = 0
#     energy = K
#
#     for val in M_li:
#         if M_li[0] == val:
#             energy= K-val
#             if energy <0:
#                 break
#
#         if M_li.index(val) != len(M_li) - 1:
#             if energy >= M_li[M_li.index(val)+1] - M_li[M_li.index(val)]:
#                 pass
#             elif M_li[M_li.index(val)+1] - M_li[M_li.index(val)] > K:
#                 count = 0
#                 break
#             elif energy < M_li[M_li.index(val)+1] - M_li[M_li.index(val)]:
#                 count+=1
#                 energy=K
#             energy -= M_li[M_li.index(val) + 1] - M_li[M_li.index(val)]
#
#         elif M_li.index(val) == len(M_li) - 1:
#             if energy >= N - val:
#                 pass
#             elif energy < N - val:
#                 count += 1
#                 energy = K
#             elif N - val > K:
#                 count = 0
#                 break
#
#
#     print(f'#{t} {count}')
#
#

# for i in range(N+1):
#     if i in M_li:
#         if M_li.index(i) != len(M_li)-1:
#             if energy >= M_li[M_li.index(i)+1]-M_li[M_li.index(i)]:
#                 pass
#             elif M_li[M_li.index(i)+1]-M_li[M_li.index(i)]> K:
#                 count = 0
#                 break
#             elif energy < M_li[M_li.index(i)+1]-M_li[M_li.index(i)]:
#                 count+=1
#                 energy=K
#         elif M_li.index(i) == len(M_li)-1:
#             if energy >= N-i:
#                 pass
#             elif energy < N-i:
#                 count+=1
#                 energy=K
#             elif N-i > K:
#                 count= 0
#                 break
#     energy -= 1
#
# print(f'#{t} {count}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1,T+1):

    K, N, M = map(int,input().split())

    li = list(map(int, input().split()))

    li.append(N)

    i = count = start = last = 0

    while i < N+1:
        if li[i] - start <=K:
            last = li[i]
            i += 1
        else:
            if li[i] -last >K:
                ans = 0
                break
            else:
                start = last
                count += 1

    print(f'{t} {count}')