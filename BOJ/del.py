def BinarySort(a, n, idx):
    start = a[0]
    end = a[-1]
    cnt = 0
    while start<=end:
        cnt += 1
        middle = n // 2

        if a[middle] < idx:
            start = a[middle]
        elif a[middle] > idx:
            end = a[middle]
        elif a[middle] == idx:
            return cnt

T = int(input())

for t in range(1,T+1):

    N, D = map(int, input().split())
    li = list(map(int, input().split()))

    result = BinarySort(li,N,D)
        

    print(f'#{t} {res}')