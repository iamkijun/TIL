# def BinarySort(a, start, end, idx):
#     while start<=end:
#         middle = (start+end) // 2
#         if a[middle] == idx:
#             return middle+1
#         elif a[middle] > idx:
#             end = middle -1
#         elif a[middle] < idx:
#             start = middle +1
#     return 0

T = int(input())

for t in range(1,T+1):

    N, D = map(int, input().split())
    li = list(map(int, input().split()))

    # result = BinarySort(li,0,N-1,D)
    try:
        result = li.index(D)
        print(f'#{t} {result}')
    except:
        print(f'#{t} 0')