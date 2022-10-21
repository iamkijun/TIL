import sys
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

count = 0

# for j in range(60):
#     if j % 10 == K or j//10 == K:
#         count += 1

# count = count*120 - count**2

# h_count = 0

# for i in range(N):
#     if i % 10 == K or i // 10 ==K:
#         h_count += 1

# if h_count == 0:
#     count = (N+1) * count
# if h_count > 0:
#     count = count*(N+1-h_count) + 3600*h_count
# print(count)

for i in range(N+1):
    if i <10:
        h = '0'+str(i)
    else:
        h = str(i)
    for j in range(60):
        if j < 10:
            m = '0' + str(j)
        else:
            m = str(j)
        for k in range(60):
            if k < 10:
                s = '0' + str(k)
            else:
                s = str(k)
            
            if str(K) in h or str(K) in m or str(K) in s:
                count += 1

print(count)