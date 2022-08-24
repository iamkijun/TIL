import sys
sys.stdin = open('IM추천문제/input.txt','r')

li = list(map(int, input().split()))

#[1,2,3,4,5]가 될 때 까지 반복
while li != [1,2,3,4,5]:
    for i in range(4):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            print(*li)
