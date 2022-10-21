import sys
sys.stdin = open('input.txt','r')
input= sys.stdin.readline

N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for n in range(1,N+1):
    
    y1,x1,y2,x2 = map(int,input().split())

    # for j in range(y1, y1+y2):
    #     for i in range(x1, x1+x2):
    #         arr[i][j] = n

    for i in range(y1, y1+y2):
        arr[i][x1:x1+x2] = [n] * x2

    

area = [0] * (N+1)

for i in range(1001):
    for j in range(1001):
        if arr[i][j]:
            area[arr[i][j]] +=1

for i in range(1,N+1):
    print(area[i])

# for n in range(1,N+1):
#     cnt = 0
#     for m in arr:
#         cnt += m.count(n)
#     print(cnt)

# for n in range(1, N+1):
#     ans = 0
#     for i in range(1001):
#         ans += arr[i].count(n)
#     print(ans)