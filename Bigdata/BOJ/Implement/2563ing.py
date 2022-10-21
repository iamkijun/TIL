import sys
sys.stdin = open('input.txt','r')

N = int(input())

li = []

for _ in range(N):
    x, y = map(int,input().split())
    li.append([x,y])

print(li)

total = 0

for i in range(1<<N):
    li_two = []
    for j in range(N):
        if i & (1<<j):
            li_two.append(li[j])


    if len(li_two)==2:

        if abs(li_two[0][0] -li_two[1][0]) <= 10 and abs(li_two[0][1] -li_two[1][1]) <= 10:

            total += ((10 - abs(li_two[0][0] -li_two[1][0])) * (10 - abs(li_two[0][1] -li_two[1][1])))

print(len(li)*100 - total)