import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())
K = int(input())
li = list(map(int,input().split()))

li.sort()
if N>K:
    dif = []
    for i in range(1,N):
        dif.append(li[i]-li[i-1])

    dif.sort()

    for _ in range(K-1):
        dif.pop(-1)

    print(sum(dif))
else:
    print(0)