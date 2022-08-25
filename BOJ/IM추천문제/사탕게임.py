이거 못품 ㅠㅠ
# import sys
# sys.stdin = open('input.txt','r')

# N = int(input())

# arr = [[0]*(N+2)] + [[0] + list(map(str, input())) + [0] for _ in range(N)] + [[0]*(N+2)]

# max_len = 0

# #상하좌우
# di = [-1,1,0,0]
# dj = [0,0,-1,1]

# #[1] 행 비교
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         for d in range(4):
#             arr[i][j], arr[i+di[d]][j+dj[d]] = arr[i+di[d]][j+dj[d]], arr[i][j] #인접한거 교환
#             for k in range(N,0,-1):
#                 for x in range(1,N-k+1):
#                     if len(set(arr[i][j:j+k])) == 1:
#                         if k > max_len:
#                             max_len = k
#                             break
#                         elif k<= max_len:
#                             break
#             arr[i][j], arr[i+di[d]][j+dj[d]] = arr[i+di[d]][j+dj[d]], arr[i][j] #원상복구

# #[2] 전치행렬
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# # 
# #[3] 열 비교
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         for d in range(4):
#             arr[i][j], arr[i+di[d]][j+dj[d]] = arr[i+di[d]][j+dj[d]], arr[i][j] #인접한거 교환
#             for k in range(N-j,0,-1):
#                 for x in range(1,N-k+1):
#                     if len(set(arr[i][j:j+k])) == 1:
#                         if k > max_len:
#                             max_len = k
#                             break
#                         elif k<= max_len:
#                             break
#             arr[i][j], arr[i+di[d]][j+dj[d]] = arr[i+di[d]][j+dj[d]], arr[i][j] #원상복구


# print(max_len)

