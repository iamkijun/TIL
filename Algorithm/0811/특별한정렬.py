import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def selectionSort(a,N):
    for i in range(N-1):
        maxIdx = i
        minIdx = i
        if i % 2 == 0:
            for j in range(i+1,N):
                if a[maxIdx] < a[j]:
                    maxIdx = j
            a[i], a[maxIdx] = a[maxIdx], a[i]

        elif i % 2 == 1:
            for j in range(i+1,N):
                if a[minIdx] > a[j]:
                    minIdx = j
            a[i], a[minIdx] = a[minIdx], a[i]

    return a

for t in range(1,T+1):
    N = int(input())

    li = list(map(int,input().split()))

    sorted_li = selectionSort(li, N)

    print(f'#{t} ',*sorted_li[:10])
