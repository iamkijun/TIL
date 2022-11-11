import sys
sys.stdin = open("Greedy/input.txt","r")

# N, K = map(int, input().split())

# S = input()

# h_list = []
# for i in range(len(S)):
#     if S[i] == 'H':
#         h_list.append(1)
#     else:
#         h_list.append(0)

# cnt = 0 

# for i in range(K):
#     if h_list[i] == 0:
#         for j in range(i,K+1):
#             if h_list[j] == 1:
#                 cnt += 1
#                 # print(i)
#                 h_list[j] += 1
#                 break


# for i in range(K,len(S)-K):
#     if h_list[i] == 0:
#         for j in range(-K,K+1):
#             if h_list[i+j] == 1:
#                 cnt += 1
#                 # print(i)
#                 h_list[i+j] += 1
#                 break

# for i in range(len(S)-K, len(S)):
#     if h_list[i] == 0:
#         for j in range(-K,1):
#             if h_list[i+j] == 1:
#                 cnt += 1
#                 # print(i)
#                 h_list[i+j] += 1
#                 break

# # print(h_list)
# print(cnt)

N, K = map(int, input().split())

placement = list(input())

ans = 0

for i in range(N):
    if placement[i] == 'P':
        for i in range(max(i-K, 0), min(i+K+1, N)):
            if placement[i] == 'H':
                placement[i] = 0
                ans += 1
                break
print(ans)