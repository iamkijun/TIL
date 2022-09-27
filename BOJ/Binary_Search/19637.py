import sys
sys.stdin = open('Binary_Search/input.txt','r')

N, M = map(int, input().split())

arr =[]

for n in range(N):
    li = list(input().split())
    arr.append(li)

for m in range(M):
    num = int(input())

    for val in arr:
        if num <= int(val[1]):
            print(val[0])
            break
        else:
            continue





