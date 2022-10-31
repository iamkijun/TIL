import sys
sys.stdin = open('Prefix_Sum/input.txt','r')

N, M = map(int, input().split())

arr = []

for n in range(N):
    li = [0]+ list(map(int, input().split()))

    prefix_sum = []
    temp = 0
    for i in li:
        temp += i
        prefix_sum.append(temp)

    arr.append(prefix_sum)

K = int(input())
for m in range(K):
    si,sj, ei,ej = map(int,input().split())
    si,ei= si-1,ei-1
    ans = 0
    
    for i in range(si, ei+1):
        ans += (arr[i][ej] - arr[i][sj-1])
    print(ans)