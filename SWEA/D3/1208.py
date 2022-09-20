import sys
sys.stdin = open('D3/input.txt','r')

# for t in range(1,11):
#     dump = int(input())
 
#     li = list(map(int, input().split()))
 
#     for i in range(dump):
#         li.sort()
#         li[0] += 1
#         li[-1] -= 1
#         if li[-1] - li[0] <= 1:
#             break
 
#     li.sort()
#     diff = li[-1] - li[0]
 
#     print(f'#{t} {diff}')

for t in range(1,11):

    N = int(input())

    li = list(map(int, input().split()))

    for _ in range(N):
        
        for i in range(99,0,-1):
            for j in range(0,i):
                if li[j] >li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]

        li[-1] -=1
        li[0] +=1

    for i in range(99,0,-1):
            for j in range(0,i):
                if li[j] >li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
        

    print(f'#{t} {li[-1] - li[0]}')
        